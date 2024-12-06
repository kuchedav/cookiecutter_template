import getpass
import platform
from re import sub
import subprocess
import sys
from pathlib import Path
import os
from daves_utilities.david_secrets import decrypt_message

OPERATING_SYSTEM = platform.system()
if OPERATING_SYSTEM == "Windows":
    PYTHON_PATH = "env/Script/python.exe"
    PIP_PATH = "env/Script/pip.exe"
    PRE_COMMIT_PATH = "env/Script/pre-commit.exe"
else:
    PYTHON_PATH = "env/bin/python"
    PIP_PATH = "env/bin/pip"
    PRE_COMMIT_PATH = "env/bin/pre-commit"


print("set author")
author_name = getpass.getuser()
pythonproject_toml = Path("pyproject.toml")
pythonproject_toml.write_text(
    pythonproject_toml.read_text().replace("<AUTHOR_NAME>", author_name)
)

########################################################################################
# GIT init                                                                             #
########################################################################################
print("Initialize git")
try:
    subprocess.run(["git","init","."], check=True)
    subprocess.run(["git","checkout","-b","main"], check=True)
except subprocess.CalledProcessError:
    print("Error: Failed to initialize the repository with git!")
    sys.exit(1)

########################################################################################
# VENV                                                                                 #
########################################################################################
print("create environment with python 3.13")
try:
    subprocess.run(["python3.13","-m","venv","env"], check=True)
except subprocess.CalledProcessError:
    print("Error: Failed to create environment!")
    sys.exit(1)

# Activate the virtual environment
if os.name == 'nt':  # Windows
    activate_script = os.path.join("env", "Scripts", "activate")
else:  # Unix or MacOS
    activate_script = os.path.join("env", "bin", "activate")

print(f"Create {'pip.ini' if os.name == 'nt' else 'pip.conf'}")

########################################################################################
# Package install                                                                      #
########################################################################################

print("Upgrade pip and install uv")
try:
    subprocess.run([
        PYTHON_PATH, "-m", "pip", "install", "--upgrade", "pip", "uv"
    ], check=True)
except subprocess.CalledProcessError:
    print("Error: Failed to upgrade pip and install uv!")
    sys.exit(1)

print("Install project as package")
try:
    subprocess.run([
        PYTHON_PATH, "-m", "uv", "pip", "install", "-e", ".[dev]"
    ], check=True)
except subprocess.CalledProcessError:
    print("Error: Failed to install project as package!")
    sys.exit(1)

print("uv install requirements")

requirements_path = Path("requirements.txt")
if requirements_path.is_file():
    try:
        subprocess.run([
            PYTHON_PATH, "-m", "uv", "pip", "install", "-r", "requirements.txt"
        ], check=True)
    except subprocess.CalledProcessError:
        print("Error: Failed to install packages using uv!")
        sys.exit(1)
else:
    print("requirements.txt not found, skipping installation.")

########################################################################################
# pre-commit                                                                           #
########################################################################################
print("setup pre-commit hook scripts")
try:
    subprocess.run([
        PRE_COMMIT_PATH, "install"
    ], check=True)
except subprocess.CalledProcessError:
    print("Error: Failed to setup git hook scripts!")
    sys.exit(1)

########################################################################################
# GIT initial commit                                                                   #
########################################################################################
print("initial commit")
try:
    for i in range(2):
        if OPERATING_SYSTEM == "Windows":
            subprocess.run([
                r"env\Scripts\activate",
                "&&",
                "git",
                "add",
                "*",
                "&&",
                "git",
                "commit",
                "-m",
                "'initial commit'",
            ], shell=True, check=bool(i))
        else:
            subprocess.run([". ./env/bin/activate && git add . && git commit -m 'initial commit'"],
            shell=True, check=bool(i))
except subprocess.CalledProcessError:
    print("Error: Failed to do initial commit!")
    sys.exit(1)
