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

new_conclusion = """## 6. Conclusion et Perspectives\n\nCe projet illustre de bout en bout la démarche d'adaptation de domaine pour un grand modèle de langage. Au-delà de la simple exécution technique, il démontre que des modèles relativement légers (comme DistilGPT-2) peuvent capter une sémantique très spécialisée si on leur fournit un corpus de qualité, sans nécessiter d'infrastructures de calcul démesurées.\n\n### Limites de l'approche et pistes d'amélioration\n\nL'approche adoptée ici, bien que fonctionnelle, correspond à un *full fine-tuning*, où l'intégralité des poids du modèle est mise à jour. C'est une stratégie assez coûteuse computationnellement.\n\nPour une évolution naturelle de ce projet, je me tournerais aujourd'hui vers les méthodes **PEFT (Parameter-Efficient Fine-Tuning)**, et plus particulièrement **LoRA (Low-Rank Adaptation)**. Au lieu de recalculer tous les paramètres, on gèle le modèle pré-entraîné et on injecte des matrices de rang faible dans les couches d'attention. Couplé à de la quantification sur 4 bits (**QLoRA**), cela permettrait de spécialiser des modèles beaucoup plus massifs (comme Llama-3 8B) sur des machines grand public, ouvrant la porte à des performances de pointe."""

if idx_concl != -1:
    nb.cells[idx_concl].source = new_conclusion

save_notebook(nb, "FineTunning.ipynb")
print("Task 5 complete.")
