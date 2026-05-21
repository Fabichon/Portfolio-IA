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

comp_md = """### Évaluation comparative : Avant vs Après\n\nLa véritable preuve de l'efficacité du fine-tuning réside dans la comparaison directe. Nous allons charger le modèle `distilgpt2` d'origine (non entraîné sur notre corpus) et lui soumettre les mêmes prompts. Cela nous permettra de constater empiriquement le changement de registre sémantique."""

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
