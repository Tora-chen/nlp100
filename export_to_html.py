import nbformat
from nbconvert import HTMLExporter
from pathlib import Path

# 获取 notebooks
paths = [p for p in Path("./ja").glob("*.ipynb")]
names = [p.stem for p in paths]
books = [
    nbformat.read(path, as_version=4)
    for path in paths
]

# 转换成 HTML
exporter = HTMLExporter()
pages = [
    exporter.from_notebook_node(book)[0] for book in books
]

# 写出
for i in range(0, len(books)):
    with open(f"./html/{names[i]}.html", "w", encoding="utf-8") as f:
        f.write(pages[i])
