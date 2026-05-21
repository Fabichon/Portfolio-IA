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

loss_md = """### Visualisation de la convergence\n\nPour s'assurer que le modèle a bien appris la distribution de notre corpus, on trace l'évolution de la fonction de perte (Cross-Entropy Loss) sur nos étapes d'entraînement. Une courbe décroissante valide notre approche d'optimisation."""

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
