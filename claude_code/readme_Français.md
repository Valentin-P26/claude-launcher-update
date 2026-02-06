# Claude Code - Lanceur automatique

Script Python qui met à jour et lance Claude Code automatiquement via un raccourci système sur Ubuntu.

## 📋 Description

Ce projet permet de :
1. Mettre à jour Claude Code avec la dernière version
2. Lancer Claude Code avec Ollama
3. Le tout en tapant simplement "claude" dans le menu de recherche Ubuntu

## 🚀 Installation

### Prérequis

Avant de commencer, assure-toi d'avoir :

- Ubuntu (ou distribution Linux basée sur Debian)
- Python 3
- Menu Editor (MenuLibre)
- **Ollama** : [Installation d'Ollama](https://ollama.com/download/linux)
- **Un modèle LLM** installé dans Ollama (exemple : `qwen2.5-coder:7b`)
```bash
ollama pull qwen2.5-coder:7b
```
- **Claude Code** : [Installation de Claude Code](https://code.claude.com/docs/en/overview)
- Connexion Internet (pour les mises à jour)

### Étape 1 : Créer le script Python

Crée un fichier `start_claude.py` avec ce contenu :
```python
import subprocess

# Mise à jour de Claude Code
print("🔄 Mise à jour de Claude Code...")
subprocess.run('curl -fsSL https://claude.ai/install.sh | bash', shell=True)

print("\n🚀 Lancement de Claude Code...")
# Lancement de Claude Code avec Ollama
subprocess.run("ollama launch claude", shell=True)
```

Donne-lui les permissions d'exécution :
```bash
chmod +x start_claude.py
```

### Étape 2 : Installer Menu Editor
```bash
sudo apt update
sudo apt install menulibre
```

### Étape 3 : Configurer le raccourci

1. Ouvre Menu Editor :
   - Appuie sur la touche **Super (Windows)**
   - Tape "menulibre" et ouvre l'application

2. Créer une nouvelle entrée :
   - Clique sur le bouton **"+"**
   - Sélectionne **"Add Launcher"**

3. Remplir les champs :
   - **Name** : `Claude Code`
   - **Command** : `gnome-terminal -- python3 /chemin/vers/ton/dossier/start_claude.py`
   - **Working Directory** : `/chemin/vers/ton/dossier`
   - **Icon** : Choisis une icône (terminal, code, ou claude)
      - **Options** :
     - ✅ **Run in terminal**
     - ✅ **Use startup notification**

4. Sauvegarde avec l'icône **⬇️**

## 💻 Utilisation

### Méthode : Via le menu Ubuntu
1. Appuie sur la **touche Super (Windows)**
2. Tape **"claude"**
3. Clique sur l'application qui apparaît

## 📁 Structure du projet
```
claude/
├── start_claude.py    # Script principal
└── README.md          # Le fichier explicatif
```

## 🔧 Le script fait quoi ?

1. **Mise à jour automatique** :
   - Exécute `curl -fsSL https://claude.ai/install.sh | bash`
   - Télécharge et installe la dernière version de Claude Code

2. **Lancement** :
   - Exécute `ollama launch claude`
   - Lance Claude Code via Ollama

## 📝 Notes

- La mise à jour nécessite une connexion Internet
- Le script peut prendre quelques secondes
- Remplace les chemins par ton chemin personnel

## 🔗 Liens utiles

- [Claude AI](https://claude.ai)
- [Ollama](https://ollama.ai)
- [Documentation Claude Code](https://docs.claude.com)

## 👤 Auteur

Valentin Parmentier

## 📄 Licence

Ce projet est libre d'utilisation.