# Fine-Tuning de LLM : Adaptation de Domaine (Aérospatiale)

Ce projet illustre le processus complet de **Fine-Tuning d'un modèle de langage (LLM)** pour le spécialiser dans un domaine technique complexe : l'aérospatiale. 

L'objectif est de démontrer comment un modèle généraliste léger peut acquérir une expertise sémantique pointue grâce à une sélection rigoureuse de données et une stratégie d'entraînement adaptée.

## 🚀 Points Clés du Projet

- **Architecture** : Utilisation de **DistilGPT-2** (82M de paramètres), un modèle compact et efficace de la famille GPT.
- **Data Engineering** : Extraction automatisée d'un corpus spécialisé via l'API Wikipedia sur des thématiques précises (Ariane 6, propulsion cryogénique, mécanique orbitale).
- **Entraînement** : Mise en œuvre du **Causal Language Modeling (CLM)** avec l'écosystème Hugging Face (`transformers`, `datasets`).
- **Analyse Comparative** : Évaluation empirique des performances en comparant le modèle de base et le modèle spécialisé sur des prompts techniques.

## 📊 Résultats & Pédagogie

Le notebook est conçu pour être un support pédagogique autant qu'une démonstration technique :
- **Visualisation de la convergence** : Graphique de la *Training Loss* via Matplotlib.
- **Gestion des répétitions** : Implémentation de stratégies de décodage (pénalité de répétition, n-gram blocking) pour optimiser la qualité du texte généré.
- **Explications Théoriques** : Focus sur la tokenization BPE et les enjeux du sur-apprentissage sur de petits corpus.

## 🛠️ Stack Technique

- **Langage** : Python
- **Bibliothèques** : Hugging Face Transformers, PyTorch, Wikipedia-API, Matplotlib, Nbformat
- **Environnement** : Jupyter Notebook / Google Colab (support GPU)

## 📈 Perspectives

Le projet se conclut par une ouverture sur les techniques modernes de fine-tuning efficace, notamment **LoRA (Low-Rank Adaptation)** et **QLoRA**, illustrant une veille technologique active sur les méthodes d'adaptation de modèles massifs à moindre coût computationnel.

---
*Projet réalisé dans le cadre du Master 1 Mathématiques Appliquées au Calcul et à l'IA (MACIA).*

---

# Deep Pricing : Approximation de Black-Scholes par Réseaux de Neurones

Ce second projet explore l'intersection entre la **Finance Quantitative** et le **Deep Learning**. L'objectif est de remplacer le calcul analytique traditionnel de la formule de Black-Scholes par une approximation neuronale ultra-rapide.

## 🚀 Points Clés du Projet

- **Architecture** : Réseau de neurones Feed-Forward (PyTorch) avec 2 couches cachées et activations ReLU.
- **Expertise Quant** : Analyse fine de l'erreur par **Moneyness** ($S/K$), permettant de valider la précision du modèle sur les options *At-the-Money*, *In-the-Money* et *Out-of-the-Money*.
- **Performance** : Benchmark comparatif entre l'inférence neuronale et le calcul analytique, démontrant un gain de vitesse significatif pour le pricing de masse.
- **Analyse des Résidus** : Étude de la normalité des erreurs et diagnostic de biais pour garantir la fiabilité financière du modèle.

## 🛠️ Stack Technique

- **Langage** : Python
- **Bibliothèques** : PyTorch, Scikit-Learn, Pandas, Matplotlib, Seaborn
- **Concepts Finance** : Modèle de Black-Scholes, Options Call européennes, Volatilité implicite, Taux sans risque.

---
*Projet réalisé dans le cadre du Master 1 Mathématiques Appliquées au Calcul et à l'IA (MACIA).*
