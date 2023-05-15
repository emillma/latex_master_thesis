from pathlib import Path

chap_dir = Path(__file__).parents[1] / "chapters"
out_file = chap_dir / "include.tex"
index_name = "__include__.tex"
todo_dir = [chap_dir]


def make_index_file(dir: Path):
    files = [p.relative_to(chap_dir) for p in sorted(dir.glob("[!_][!_].tex"))]
    (dir / index_name).write_text("\n".join(r"\input{" + str(f) + "}" for f in files))


dirs = [p for p in chap_dir.glob("*") if p.is_dir()]
print(dirs)
for d in dirs:
    make_index_file(d)

# rel_path = .relative_to(chap_dir.parent)
# out += r"\input{" + str(rel_path) + "}\n"

# out_file.write_text(out)
