"""
Script d'installation
"""

import logging
import os
import shutil
import subprocess

VENV = "Formation"
PIP = f"./{VENV}/Scripts/pip.exe"

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def init():
    installation_venv()
    copie_fichier()
    installation_Lib()
    final()

def installation_venv():
    try:
        logging.info("Création du venv en cours...")
        subprocess.run(["python", "-m", "venv", VENV])
    except Exception as e:
        logging.error("Erreur lors de la création du venv")
    
def copie_fichier():
    try:
        logging.info("Copie des fichiers en cours...")
        shutil.copytree("src", f"{VENV}/src", dirs_exist_ok=True)
        shutil.copyfile("pytest.ini", f"{VENV}/pytest.ini")
    except Exception as e:
        logging.error("Erreur lors de la copie des fichiers")

def installation_Lib():
    try:
        logging.info("Installation des librairies en cours...")
        subprocess.run([PIP, "install", "pytest"])
        subprocess.run([PIP, "install", "pytest-bdd"])
        subprocess.run([PIP, "install", "selenium"])
        subprocess.run([PIP, "install", "faker"])
    except Exception as e:
        logging.error("Erreur lors de l'installation des librairies")
        logging.error(e)

def final():
    try:
        logging.info("Installation terminée")
        logging.info("Ouverture de powershell")
        subprocess.run(["powershell.exe", "-Command", f"Start-Process powershell.exe -ArgumentList '-NoExit', '-Command', '.\{VENV}\Scripts\Activate.ps1;', 'cd {VENV};', 'pytest'"])
    except Exception as e:
        logging.error("Erreur lors de l'ouverture de powershell")
        
if __name__ == "__main__":
    init()
    