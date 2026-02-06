import subprocess
import sys
import select

print("Launching Claude Code in 10 seconds...")
print("Type 'update' to launch the update")

# Attendre 10 secondes pour une entrée utilisateur
t = select.select([sys.stdin], [], [], 10)

# Vérifier si l'utilisateur a tapé 'update'
if t[0] and sys.stdin.readline().strip().lower() == 'update':
    do_update = True
else:
    do_update = False

# Si mise à jour demandée, exécuter le script d'installation
if do_update:
    print("🔄 Updating...")
    subprocess.run('curl -fsSL https://claude.ai/install.sh | bash', shell=True)

# Lancer Claude Code
subprocess.run("ollama launch claude", shell=True)