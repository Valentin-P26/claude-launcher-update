import subprocess

# Mise à jour de Claude Code
print("🔄 Mise à jour de Claude Code...")
subprocess.run('curl -fsSL https://claude.ai/install.sh | bash', shell=True)

print("\n🚀 Lancement de Claude Code...")
# Lancement de Claude Code avec Ollama
subprocess.run("ollama launch claude", shell=True)