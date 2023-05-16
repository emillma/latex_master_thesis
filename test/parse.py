from pathlib import Path
from xml.etree import ElementTree as ET
from html.parser import HTMLParser
import re


class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.data = []
        self.current = None
        self.tag_stack = []
        self.class_stack = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        self.tag_stack.append(tag)
        self.class_stack.append(attrs_dict.get("class", None))
        if tag == "tr":
            self.current = {}
        if m := re.match(r"This topic has (\d+) replies", attrs_dict.get("title", "")):
            self.current["replies"] = m.group(1)
        if topic_id := attrs_dict.get("data-topic-id", None):
            self.current["topic_id"] = topic_id

    def handle_endtag(self, tag):
        self.tag_stack.pop()
        self.class_stack.pop()
        if tag == "tr":
            self.data.append(self.current)

    def handle_data(self, data):
        current_class = self.class_stack[-1]
        if current_class == "title raw-link raw-topic-link":
            self.current["title"] = data


parser = MyHTMLParser()
file = Path(__file__).parent / "forum_history.html"
parser.feed(file.read_text())
posts = parser.data
keywords = [r"[^\w]pps", "flash", "boot", "compil", "kernel"]
posts_pps = [
    p for p in posts if any(re.search(k, p["title"].lower()) for k in keywords)
]

posts_pps = sorted(posts_pps, key=lambda p: p["title"])


# {'‘':"'",
#  "”":'"',
#  "…":
#  }
def process_title(title):
    title = title.replace("_", f"\\_")
    title = title.replace("[", "{[}")
    title = title.replace("]", "{]}")
    # totle = re.sub(r"(\[.*?\])", r"{\1}", title)
    return title


titles = [f"{process_title(p['title'])}" for p in posts_pps]
replies = [p["replies"] for p in posts_pps]
topic_ids = [p["topic_id"] for p in posts_pps]
out = "\\\\\n".join("&".join([t, r, i]) for t, r, i in zip(titles, replies, topic_ids))

# \\begin{{tabular}}{{lrr}}
# \\end{{tabular}}
out = f"""
\\begin{{longtable}}{{p{{.8\\textwidth}}rr}}
Title & Comments & ID \\\\
\\hline\\\\
    
{out}
\\end{{longtable}}
"""
Path(__file__).parent.joinpath("forum_history.tex").write_text(out)
