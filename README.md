# 🤖 Portfolio IA & Data Science 

Bienvenue dans mon portfolio technique. Ce dépôt regroupe des projets avancés illustrant mes compétences en **Machine Learning**, **Finance Quantitative** et **Natural Language Processing (NLP)**.

Chaque projet est conçu avec une approche rigoureuse : de la théorie mathématique à l'implémentation optimisée, avec une attention particulière à la pédagogie et à la visualisation des résultats.

---

## 🚀 Projets Principaux

### 1. Fine-Tuning de LLM : Adaptation de Domaine (Aérospatiale)
**Démonstration de la spécialisation d'un modèle GPT-2 sur un corpus technique.**

*   **Objectif** : Transformer un modèle généraliste en expert du domaine spatial.
*   **Pipeline** : 
    *   **Data Engineering** : Création d'un corpus sur-mesure de ~236k caractères via l'API Wikipedia (Ariane 6, propulsion, mécanique orbitale).
    *   **Architecture** : Fine-tuning de **DistilGPT-2** via Hugging Face `Transformers`.
    *   **Innovation** : Implémentation de fixes robustes pour le multiprocessing et la conformité API.
*   **Résultat** : Une réduction nette de la perplexité sur le domaine cible et une génération de texte techniquement cohérente.
*   **[Lien vers le Notebook](./FineTunning.ipynb)**

### 2. Deep Pricing : Approximation de Black-Scholes par Réseaux de Neurones
**Optimisation du pricing d'options financières via le Deep Learning.**

*   **Objectif** : Remplacer le calcul analytique de Black-Scholes par une inférence neuronale ultra-rapide.
*   **Approche** :
    *   **Modélisation** : Réseau Feed-Forward sous `PyTorch` avec analyse par **Moneyness** ($S/K$).
    *   **Validation** : Analyse des résidus et benchmark de performance (Vitesse vs Précision).
*   **Résultat** : Une précision de pricing quasi-analytique avec un gain de temps de calcul significatif pour les simulations de masse.
*   **[Lien vers le Notebook](./Deep_Pricing_Black_Scholes_NN_PERSO.ipynb)**

---

## 🛠️ Stack Technique & Expertise

| Domaine | Technologies |
| :--- | :--- |
| **Deep Learning** | PyTorch, Transformers (Hugging Face), Scikit-Learn |
| **Data Engineering** | Pandas, NumPy, Wikipedia-API, Scrapping |
| **Visualisation** | Matplotlib, Seaborn |
| **Théorie** | Mathématiques Financières, NLP (BPE, CLM), Optimisation (Adam) |

---

## 🎓 Parcours Académique
Projets réalisés dans le cadre du **Master 1 Mathématiques Appliquées au Calcul et à l'IA (MACIA)**. Ils illustrent une capacité à traduire des concepts théoriques complexes en solutions logicielles concrètes et performantes.
[Contact/LinkedIn]*
