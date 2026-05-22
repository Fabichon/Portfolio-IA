# FineTuning Portfolio Enhancement Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Transform `FineTunning.ipynb` into a pedagogical showcase piece by adding theoretical explanations, loss visualization, comparative results, and modern perspectives, all written in a natural, academic Master 1 tone.

**Architecture:** Modifying Jupyter Notebook cells using a Python script with `nbformat` to ensure JSON integrity, appending new markdown and code cells at specific locations.

**Tech Stack:** Python, `nbformat`, `matplotlib`, `transformers`

---

### Task 1: Setup script for safe notebook modification

**Files:**
- Create: `scripts/modify_notebook.py`

- [ ] **Step 1: Write the modification script skeleton**

```python
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
```

- [ ] **Step 2: Run to verify**
Run: `python scripts/modify_notebook.py`
Expected: Output "Notebook modification utilities ready."

- [ ] **Step 3: Commit**
```bash
git add scripts/modify_notebook.py
git commit -m "chore: add notebook modification utilities"
```

### Task 2: Add pedagogical encadrés (BPE and block size)

**Files:**
- Create: `scripts/task2_add_explanations.py`
- Modify: `FineTunning.ipynb`

- [ ] **Step 1: Write the script to insert pedagogical cells**

```python
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

bpe_explanation = """**Focus théorique : Le Byte Pair Encoding (BPE)**\\n\\nLe choix du tokenizer n'est pas anodin. Le BPE est un algorithme de compression de données qui trouve un compromis élégant entre une tokenization par mot (vocabulaire immense, gestion difficile des mots inconnus) et par caractère (séquences trop longues, perte de sens). Il fusionne itérativement les paires de caractères les plus fréquentes pour construire un vocabulaire sous-mot. Cela permet au modèle de traiter efficacement le vocabulaire technique aérospatial même s'il n'a pas rencontré tous les mots exacts lors de son pré-entraînement."""

if idx_tok != -1:
    add_markdown_cell(nb, idx_tok + 1, bpe_explanation)

# Reload idx since we inserted a cell
idx_clm = -1
for i, cell in enumerate(nb.cells):
    if "## 4. Configuration et fine-tuning" in cell.source:
        idx_clm = i
        break

block_explanation = """**Pourquoi des blocs de 128 tokens ?**\\n\\nDans notre approche, les textes sont concaténés puis découpés en fenêtres de taille fixe (128 tokens). Cette méthode, classique en Causal Language Modeling (CLM), garantit que le modèle reçoit des tenseurs de dimensions constantes sans avoir recours à un remplissage excessif (padding). Bien que l'on perde occasionnellement le contexte exact aux frontières des blocs, cette perte est négligeable face au gain d'efficacité computationnelle lors de l'entraînement."""

if idx_clm != -1:
    add_markdown_cell(nb, idx_clm + 1, block_explanation)

save_notebook(nb, "FineTunning.ipynb")
print("Task 2 complete.")
```

- [ ] **Step 2: Execute script**
Run: `python scripts/task2_add_explanations.py`
Expected: "Task 2 complete."

- [ ] **Step 3: Commit**
```bash
git add scripts/task2_add_explanations.py FineTunning.ipynb
git commit -m "docs: add theoretical explanations on BPE and block size"
```

### Task 3: Visualize Training Loss

**Files:**
- Create: `scripts/task3_add_loss_plot.py`
- Modify: `FineTunning.ipynb`

- [ ] **Step 1: Write script to add loss visualization cell**

```python
import nbformat
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from modify_notebook import load_notebook, save_notebook, add_markdown_cell, add_code_cell

nb = load_notebook("FineTunning.ipynb")

idx_eval = -1
for i, cell in enumerate(nb.cells):
    if "## 5. Évaluation et génération de texte" in cell.source:
        idx_eval = i
        break

loss_md = """### Visualisation de la convergence\\n\\nPour s'assurer que le modèle a bien appris la distribution de notre corpus, on trace l'évolution de la fonction de perte (Cross-Entropy Loss) sur nos étapes d'entraînement. Une courbe décroissante valide notre approche d'optimisation."""

loss_code = """import matplotlib.pyplot as plt

# Extraction de l'historique d'entraînement du Trainer
history = trainer.state.log_history

# On filtre pour ne garder que les logs contenant la 'loss' (les logs d'entraînement)
steps = [log['step'] for log in history if 'loss' in log]
losses = [log['loss'] for log in history if 'loss' in log]

plt.figure(figsize=(10, 5))
plt.plot(steps, losses, marker='o', linestyle='-', color='b', linewidth=2, markersize=6)
plt.title('Évolution de la Training Loss', fontsize=14)
plt.xlabel('Étapes (Steps)', fontsize=12)
plt.ylabel('Cross-Entropy Loss', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()"""

if idx_eval != -1:
    add_markdown_cell(nb, idx_eval, loss_md)
    add_code_cell(nb, idx_eval + 1, loss_code)

save_notebook(nb, "FineTunning.ipynb")
print("Task 3 complete.")
```

- [ ] **Step 2: Execute script**
Run: `python scripts/task3_add_loss_plot.py`
Expected: "Task 3 complete."

- [ ] **Step 3: Commit**
```bash
git add scripts/task3_add_loss_plot.py FineTunning.ipynb
git commit -m "feat: add matplotlib visualization for training loss"
```

### Task 4: Base vs Fine-tuned comparison

**Files:**
- Create: `scripts/task4_add_comparison.py`
- Modify: `FineTunning.ipynb`

- [ ] **Step 1: Write script to append comparison code**

```python
import nbformat
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from modify_notebook import load_notebook, save_notebook, add_markdown_cell, add_code_cell

nb = load_notebook("FineTunning.ipynb")

idx_concl = -1
for i, cell in enumerate(nb.cells):
    if "## 6. Conclusion" in cell.source:
        idx_concl = i
        break

comp_md = """### Évaluation comparative : Avant vs Après\\n\\nLa véritable preuve de l'efficacité du fine-tuning réside dans la comparaison directe. Nous allons charger le modèle `distilgpt2` d'origine (non entraîné sur notre corpus) et lui soumettre les mêmes prompts. Cela nous permettra de constater empiriquement le changement de registre sémantique."""

comp_code = """from transformers import pipeline

# Chargement du modèle de base pour comparaison
base_generator = pipeline(
    'text-generation',
    model='distilgpt2',
    tokenizer='distilgpt2',
    device=0 if torch.cuda.is_available() else -1
)

print("="*70)
print("COMPARAISON DIRECTE : BASE vs FINE-TUNED")
print("="*70)

for i, prompt in enumerate(test_prompts, 1):
    print(f"\\n[Test {i} - Prompt: '{prompt}']")
    print("-" * 70)
    
    # Génération Base
    res_base = base_generator(prompt, max_new_tokens=40, num_return_sequences=1, temperature=0.7, pad_token_id=tokenizer.eos_token_id)
    print(f"DistilGPT-2 (Base) :\\n{res_base[0]['generated_text']}")
    print("-" * 40)
    
    # Génération Fine-Tuned
    res_ft = generator(prompt, max_new_tokens=40, num_return_sequences=1, temperature=0.7, pad_token_id=tokenizer.eos_token_id)
    print(f"DistilGPT-2 (Spécialisé) :\\n{res_ft[0]['generated_text']}")
"""

if idx_concl != -1:
    add_markdown_cell(nb, idx_concl, comp_md)
    add_code_cell(nb, idx_concl + 1, comp_code)

save_notebook(nb, "FineTunning.ipynb")
print("Task 4 complete.")
```

- [ ] **Step 2: Execute script**
Run: `python scripts/task4_add_comparison.py`
Expected: "Task 4 complete."

- [ ] **Step 3: Commit**
```bash
git add scripts/task4_add_comparison.py FineTunning.ipynb
git commit -m "feat: add direct comparison between base and fine-tuned models"
```

### Task 5: Rewrite Conclusion and Limitations

**Files:**
- Create: `scripts/task5_update_conclusion.py`
- Modify: `FineTunning.ipynb`

- [ ] **Step 1: Write script to replace conclusion text**

```python
import nbformat
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from modify_notebook import load_notebook, save_notebook

nb = load_notebook("FineTunning.ipynb")

idx_concl = -1
for i, cell in enumerate(nb.cells):
    if "## 6. Conclusion" in cell.source:
        idx_concl = i
        break

new_conclusion = """## 6. Conclusion et Perspectives\\n\\nCe projet illustre de bout en bout la démarche d'adaptation de domaine pour un grand modèle de langage. Au-delà de la simple exécution technique, il démontre que des modèles relativement légers (comme DistilGPT-2) peuvent capter une sémantique très spécialisée si on leur fournit un corpus de qualité, sans nécessiter d'infrastructures de calcul démesurées.\\n\\n### Limites de l'approche et pistes d'amélioration\\n\\nL'approche adoptée ici, bien que fonctionnelle, correspond à un *full fine-tuning*, où l'intégralité des poids du modèle est mise à jour. C'est une stratégie assez coûteuse computationnellement.\\n\\nPour une évolution naturelle de ce projet, je me tournerais aujourd'hui vers les méthodes **PEFT (Parameter-Efficient Fine-Tuning)**, et plus particulièrement **LoRA (Low-Rank Adaptation)**. Au lieu de recalculer tous les paramètres, on gèle le modèle pré-entraîné et on injecte des matrices de rang faible dans les couches d'attention. Couplé à de la quantification sur 4 bits (**QLoRA**), cela permettrait de spécialiser des modèles beaucoup plus massifs (comme Llama-3 8B) sur des machines grand public, ouvrant la porte à des performances de pointe."""

if idx_concl != -1:
    nb.cells[idx_concl].source = new_conclusion

save_notebook(nb, "FineTunning.ipynb")
print("Task 5 complete.")
```

- [ ] **Step 2: Execute script**
Run: `python scripts/task5_update_conclusion.py`
Expected: "Task 5 complete."

- [ ] **Step 3: Commit**
```bash
git add scripts/task5_update_conclusion.py FineTunning.ipynb
git commit -m "docs: rewrite conclusion with academic tone and mention PEFT/LoRA"
```
