# Design Spec: Amélioration Pédagogique de FineTunning.ipynb

## Objectif
Transformer le notebook `FineTunning.ipynb` existant en une pièce maîtresse pour un portfolio GitHub/CV, en mettant l'accent sur la pédagogie, la visualisation et la rigueur technique.

## Améliorations Prévues

1. **Encadrés Pédagogiques (Markdown)**
   - Ajouter une explication sur la Tokenization BPE (pourquoi c'est important).
   - Ajouter un paragraphe sur le choix du bloc de 128 tokens et l'architecture causale (CLM).

2. **Visualisation de la Loss (Python + Markdown)**
   - Extraire l'historique d'entraînement du `Trainer` (via `trainer.state.log_history`).
   - Ajouter une cellule générant un graphique `matplotlib` propre montrant la baisse de la "Training Loss" au fil des étapes.

3. **Comparaison Avant/Après (Python + Markdown)**
   - Charger le modèle de base (non fine-tuné) `distilgpt2`.
   - Effectuer une génération de texte avec les mêmes prompts que le modèle fine-tuné.
   - Présenter les résultats côte à côte pour prouver l'efficacité du fine-tuning sur le vocabulaire aérospatial.

4. **Section Limites et Perspectives (Markdown)**
   - Mettre à jour la section "Améliorations possibles" pour inclure des techniques modernes (PEFT, LoRA/QLoRA) qui montreraient une veille technologique active de la part du candidat.

## Contraintes
- Le format du fichier JSON (`.ipynb`) doit être respecté.
- **Ton :** Naturel, académique et rigoureux. Éviter les formulations trop formatées type "IA générative" pour privilégier une rédaction fluide, comme un étudiant de Master 1 s'adressant à ses pairs ou à un jury.
- Les textes explicatifs doivent être en français professionnel.
