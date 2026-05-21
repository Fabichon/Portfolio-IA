import nbformat
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from modify_notebook import load_notebook, save_notebook, add_markdown_cell

nb = load_notebook("FineTunning.ipynb")

# Find index of Tokenization section (contains '## 3. Tokenization')
idx_tok = -1
for i, cell in enumerate(nb.cells):
    if "## 3. Tokenization" in cell.source:
        idx_tok = i
        break

bpe_explanation = """**Focus théorique : Le Byte Pair Encoding (BPE)**\n\nLe choix du tokenizer n'est pas anodin. Le BPE est un algorithme de compression de données qui trouve un compromis élégant entre une tokenization par mot (vocabulaire immense, gestion difficile des mots inconnus) et par caractère (séquences trop longues, perte de sens). Il fusionne itérativement les paires de caractères les plus fréquentes pour construire un vocabulaire sous-mot. Cela permet au modèle de traiter efficacement le vocabulaire technique aérospatial même s'il n'a pas rencontré tous les mots exacts lors de son pré-entraînement."""

if idx_tok != -1:
    add_markdown_cell(nb, idx_tok + 1, bpe_explanation)

# Reload idx since we inserted a cell
idx_clm = -1
for i, cell in enumerate(nb.cells):
    if "## 4. Configuration et fine-tuning" in cell.source:
        idx_clm = i
        break

block_explanation = """**Pourquoi des blocs de 128 tokens ?**\n\nDans notre approche, les textes sont concaténés puis découpés en fenêtres de taille fixe (128 tokens). Cette méthode, classique en Causal Language Modeling (CLM), garantit que le modèle reçoit des tenseurs de dimensions constantes sans avoir recours à un remplissage excessif (padding). Bien que l'on perde occasionnellement le contexte exact aux frontières des blocs, cette perte est négligeable face au gain d'efficacité computationnelle lors de l'entraînement."""

if idx_clm != -1:
    add_markdown_cell(nb, idx_clm + 1, block_explanation)

save_notebook(nb, "FineTunning.ipynb")
print("Task 2 complete.")