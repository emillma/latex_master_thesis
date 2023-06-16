from pathlib import Path

root_dir = Path(__file__).parents[1]
chap_dir = root_dir / "chapters"
index_name = "__include__.tex"
todo_dir = [chap_dir]


out = ""
for d in sorted([p for p in chap_dir.iterdir() if p.is_dir()]):
    files = [p for p in sorted(d.rglob("*[!_][!_].tex"))]
    text = "\n\n".join(f.read_text() for f in files)
    d.joinpath("__all.tex").write_text(text)
# chap_dir.joinpath(index_name).write_text(out)
