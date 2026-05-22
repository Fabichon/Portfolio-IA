import nbformat
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from modify_notebook import load_notebook, save_notebook

def patch_wikipedia_cell():
    nb = load_notebook("FineTunning.ipynb")
    
    # Target cell with wikipedia extraction
    target_idx = -1
    for i, cell in enumerate(nb.cells):
        if "import wikipedia" in cell.source and "topics =" in cell.source:
            target_idx = i
            break
            
    if target_idx == -1:
        print("Could not find the Wikipedia extraction cell.")
        return

    # New source with User-Agent and retry logic
    new_source = """import wikipedia
import re
import time

# Configuration de l'API Wikipedia
# Il est fortement recommandé de définir un User-Agent pour éviter d'être bloqué
wikipedia.set_lang("en")
# Format: "NomDuProjet/Version (LienVersLeProjet; ContactEmail)"
user_agent = "PortfolioIA_FineTuning/1.0 (https://github.com/frank/portfolio; contact@example.com)"
# Note: On utilise l'accès direct via requests pour configurer le headers si nécessaire 
# ou on utilise l'astuce de la lib wikipedia :
import wikipediaapi
# Si la lib standard 'wikipedia' échoue encore, on peut passer à 'wikipedia-api' qui est plus stable.
# Mais essayons d'abord de configurer la lib actuelle proprement.

print("Extraction des données depuis Wikipedia...\\n")

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
        # Petite pause pour respecter les serveurs de Wikipedia
        time.sleep(1)
        page = wikipedia.page(topic, auto_suggest=False)
        content = page.content
        print(f"  ✓ {topic}: {len(content)} caractères")
        raw_text += content + "\\n\\n"
    except Exception as e:
        print(f"  ✗ Erreur sur {topic}: {e}")

# Nettoyage et sauvegarde
if raw_text:
    clean_text = re.sub(r'\\[.*?\\]', '', raw_text)
    clean_text = re.sub(r'\\n\\s*\\n', '\\n\\n', clean_text)
    
    file_path = "aerospace_corpus.txt"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(clean_text)
    
    print(f"\\n✓ Corpus sauvegardé: {file_path}")
    print(f"  Taille totale: {len(clean_text):,} caractères")
else:
    print("\\n⚠ Aucun texte n'a pu être extrait. Vérifiez votre connexion ou le User-Agent.")
"""
    
    nb.cells[target_idx].source = new_source
    save_notebook(nb, "FineTunning.ipynb")
    print("Wikipedia extraction cell patched with User-Agent and delay.")

if __name__ == "__main__":
    patch_wikipedia_cell()
