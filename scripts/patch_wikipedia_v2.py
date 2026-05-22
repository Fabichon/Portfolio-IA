import nbformat
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from modify_notebook import load_notebook, save_notebook

def patch_wikipedia_logic():
    nb = load_notebook("FineTunning.ipynb")
    
    # 1. Update installation cell
    for cell in nb.cells:
        if "!pip install torch wikipedia -q" in cell.source:
            cell.source = cell.source.replace("wikipedia", "wikipedia-api")
            print("Installation cell updated.")
            break
            
    # 2. Update extraction logic cell
    target_idx = -1
    for i, cell in enumerate(nb.cells):
        if "import wikipedia" in cell.source and "topics =" in cell.source:
            target_idx = i
            break
            
    if target_idx != -1:
        new_source = """import wikipediaapi
import re
import time

# Utilisation de wikipedia-api (plus stable et nécessite un User-Agent)
wiki_wiki = wikipediaapi.Wikipedia(
    language='en',
    extract_format=wikipediaapi.ExtractFormat.WIKI,
    user_agent="PortfolioIA_FineTuning/1.0 (contact@example.com)"
)

print("Extraction des données depuis Wikipedia (via Wikipedia-API)...\\n")

topics = [
    "Ariane 6",
    "Vulcain (rocket engine)",
    "Vinci (rocket engine)",
    "Rocket propulsion",
    "Orbital mechanics",
    "Hohmann transfer orbit",
    "Specific impulse",
    "Cryogenic rocket engine",
    "Space debris"
]

raw_text = ""
for topic in topics:
    try:
        # Pause pour respecter les serveurs
        time.sleep(1)
        page = wiki_wiki.page(topic)
        if page.exists():
            content = page.text
            print(f"  ✓ {topic}: {len(content)} caractères")
            raw_text += content + "\\n\\n"
        else:
            print(f"  ✗ {topic}: Page non trouvée")
    except Exception as e:
        print(f"  ✗ Erreur sur {topic}: {e}")

# Nettoyage et sauvegarde
if raw_text:
    # Suppression des références Wikipedia (ex: [12])
    clean_text = re.sub(r'\\[.*?\\]', '', raw_text)
    # Normalisation des sauts de ligne
    clean_text = re.sub(r'\\n\\s*\\n', '\\n\\n', clean_text)
    
    file_path = "aerospace_corpus.txt"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(clean_text)
    
    print(f"\\n✓ Corpus sauvegardé: {file_path}")
    print(f"  Taille totale: {len(clean_text):,} caractères")
else:
    print("\\n⚠ Aucun texte n'a pu être extrait.")
"""
        nb.cells[target_idx].source = new_source
        print("Extraction logic updated to wikipedia-api.")

    save_notebook(nb, "FineTunning.ipynb")

if __name__ == "__main__":
    patch_wikipedia_logic()
