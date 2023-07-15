import getpass
import platform
from re import sub
import subprocess
import sys
from pathlib import Path

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
print("create environment with python 3.9")
try:
    subprocess.run(["python3.9","-m","venv","env"], check=True)
except subprocess.CalledProcessError:
    print("Error: Failed to create environment!")
    sys.exit(1)

print(f"Create {'pip.ini' if OPERATING_SYSTEM=='Windows' else 'pip.conf'}")

########################################################################################
# PIP install                                                                          #
########################################################################################
print("Upgrade pip, setuptools and wheel")
try:
    subprocess.run([
        PYTHON_PATH, "-m","pip","install","--upgrade","pip","setuptools","wheel"
    ], check=True)
except subprocess.CalledProcessError:
    print("Error: Failed to upgrade pip, setuptools and wheel!")
    sys.exit(1)

print("Install requirements")
try:
    subprocess.run([
        PIP_PATH, "install", "--upgrade", "-r", "requirements.txt"
    ], check=True)
except subprocess.CalledProcessError:
    print("Error: Failed to install pip packages!")
    sys.exit(1)

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