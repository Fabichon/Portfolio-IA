import nbformat

def load_notebook(path="FineTunning.ipynb"):
    with open(path, "r", encoding="utf-8") as f:
        return nbformat.read(f, as_version=4)

def save_notebook(nb, path="FineTunning.ipynb"):
    with open(path, "w", encoding="utf-8") as f:
        nbformat.write(nb, f)

def add_markdown_cell(nb, index, source):
    new_cell = nbformat.v4.new_markdown_cell(source=source)
    nb.cells.insert(index, new_cell)

def add_code_cell(nb, index, source):
    new_cell = nbformat.v4.new_code_cell(source=source)
    nb.cells.insert(index, new_cell)

def modify_cell(nb, index, source):
    nb.cells[index].source = source

if __name__ == "__main__":
    print("Notebook modification utilities ready.")
