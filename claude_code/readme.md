# Claude Code - Automatic Launcher

Python script that automatically updates and launches Claude Code via a system shortcut on Ubuntu.

## 📋 Description

This project allows you to:
1. Update Claude Code to the latest version
2. Launch Claude Code with Ollama
3. All by simply typing "claude" in the Ubuntu search menu

## 🚀 Installation

### Prerequisites

Before starting, make sure you have:

- Ubuntu (or Debian-based Linux distribution)
- Python 3
- Menu Editor (MenuLibre)
- **Ollama**: [Ollama Installation](https://ollama.com/download/linux)
- **An LLM model** installed in Ollama (example: `qwen2.5-coder:7b`)
```bash
ollama pull qwen2.5-coder:7b
```
- **Claude Code**: [Claude Code Installation](https://code.claude.com/docs/en/overview)
- Internet connection (for updates)

### Step 1: Create the Python script

Create a `start_claude.py` file with this content:
```python
import subprocess

# Update Claude Code
print("🔄 Updating Claude Code...")
subprocess.run('curl -fsSL https://claude.ai/install.sh | bash', shell=True)

print("\n🚀 Launching Claude Code...")
# Launch Claude Code with Ollama
subprocess.run("ollama launch claude", shell=True)
```

Give it execution permissions:
```bash
chmod +x start_claude.py
```

### Step 2: Install Menu Editor
```bash
sudo apt update
sudo apt install menulibre
```

### Step 3: Configure the shortcut

1. Open Menu Editor:
   - Press the **Super (Windows)** key
   - Type "menulibre" and open the application

2. Create a new entry:
   - Click the **"+"** button
   - Select **"Add Launcher"**

3. Fill in the fields:

   **"Launcher" tab**:
   - **Name**: `Claude Code`
   - **Command**: `gnome-terminal -- python3 /path/to/your/folder/start_claude.py`
   - **Working Directory**: `/path/to/your/folder`
   - **Icon**: Optional - leave blank or select a custom .png image
   
   **"Categories" tab**:
   - ✅ Development
   - ✅ Utility
   
   **"Options" tab**:
   - ✅ **Run in terminal**
   - ✅ **Use startup notification**

4. Save with the save icon (floppy disk) in the top left corner

## 💻 Usage

### Method: Via the Ubuntu menu
1. Press the **Super (Windows)** key
2. Type **"claude"**
3. Click on the application that appears

## 📁 Project structure
```
claude/
├── start_claude.py    # Main script
└── README.md          # Documentation file
```

## 🔧 What does the script do?

1. **Automatic update**:
   - Executes `curl -fsSL https://claude.ai/install.sh | bash`
   - Downloads and installs the latest version of Claude Code

2. **Launch**:
   - Executes `ollama launch claude`
   - Launches Claude Code via Ollama

## 📝 Notes

- Updates require an Internet connection
- The script may take a few seconds
- Replace paths with your personal path

## 🔗 Useful links

- [Claude AI](https://claude.ai)
- [Ollama](https://ollama.ai)
- [Claude Code Documentation](https://docs.claude.com)

## 👤 Author

Valentin Parmentier

## 📄 License

This project is free to use.