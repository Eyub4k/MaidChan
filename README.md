# Projet Maid Chan - AI avec Voix Synthétisée en Mode "Maid"

## Description

Le projet **Maid Chan** est une application interactive utilisant une Intelligence Artificielle (IA) sous forme de chatbot avec une **réponse vocale en mode Maid** (style anime japonais). L'application permet à l'utilisateur de communiquer vocalement avec l'IA, qui répond en utilisant une voix synthétisée dans un style Maid japonais grâce à **Voicevox** et génère des réponses en utilisant un **modèle de langage Ollama**.

L'application inclut :
- **Reconnaissance vocale** pour capter l'entrée de l'utilisateur via un micro.
- **Génération de réponses** par un modèle de langage AI (Ollama).
- **Traduction automatique** du français vers le japonais via Google Translate.
- **Synthèse vocale** avec la voix de Maid Chan (Voicevox) pour répondre à l'utilisateur.

## Fonctionnalités

- **Reconnaissance vocale** : Utilisation de la bibliothèque `speech_recognition` pour écouter les commandes vocales de l'utilisateur.
- **Interaction AI** : Le modèle Ollama génère des réponses contextuelles basées sur les entrées de l'utilisateur.
- **Traduction automatique** : Utilisation de `googletrans` pour traduire les réponses générées en français vers le japonais.
- **Synthèse vocale Maid** : Utilisation de `Voicevox` pour générer une réponse vocale avec une voix de Maid en japonais.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé et configuré les éléments suivants :

- **Python 3.x** : Ce projet nécessite Python 3.
- **Docker** : Pour faire fonctionner Voicevox via Docker.
- **API Ollama** : Doit être configurée pour utiliser un modèle comme `mistral`.
- **Googletrans** : Pour la traduction automatique du texte en japonais.

### Installations nécessaires

1. **Installer les dépendances Python** :

   - Vous pouvez installer les dépendances nécessaires via `pip` :

   ```bash
   pip install -r requirements.txt
