import getpass
import platform
from re import sub
import subprocess
import sys
from pathlib import Path

from daves_utilities.david_secrets import decrypt_message, encrypt_message


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
print("create environment with python 3.11")
try:
    subprocess.run(["python3.11","-m","venv","env"], check=True)
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
        PYTHON_PATH, "-m","pip","install","--upgrade","pip","setuptools","wheel", "poetry"
    ], check=True)
except subprocess.CalledProcessError:
    print("Error: Failed to upgrade pip, setuptools, wheel and poetry!")
    sys.exit(1)

print("Install project as package")
try:
    subprocess.run([
        PYTHON_PATH, "-m","pip","install","-e",".[dev]"
    ], check=True)
except subprocess.CalledProcessError:
    print("Error: Failed to upgrade pip, setuptools, wheel and poetry!")
    sys.exit(1)

print("Poetry install requirements")
try:
    subprocess.run([
        PYTHON_PATH,"-m","poetry","install"
    ], check=True)
except subprocess.CalledProcessError:
    print("Error: Failed to install packages using poetry!")
    sys.exit(1)

password = decrypt_message(
    'gAAAAABku6ME79Pf2Uqs5VZnSPoc6NRBH2DnrsqI4wu9jNE6aML5iL5ZPpnyDy6j751SVBXL0NRAMen'
    'InYrzHAW3IK4mRy0zvVQhMTmTQ8ZD_aDa3Oq_PIs='
)
print("Poetry add credentials to publish")
try:
    subprocess.run([
        PYTHON_PATH,"-m","poetry","config","http-basic.pypi","kuchedav",f"{password}"
    ], check=True)
except subprocess.CalledProcessError:
    print("Error: Failed to install packages using poetry!")
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
