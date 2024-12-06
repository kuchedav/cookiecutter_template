import re
import sys

REPO_REGEX = r"^[a-z][-a-z0-9]+$"

repo_name = "{{ cookiecutter.repo_name }}"
author_name = "{{ cookiecutter.author_name }}"
description = "{{ cookiecutter.description }}"

if not repo_name:
    print("Error: The 'repo_name' variable is required.")
    sys.exit(1)

if not re.match(REPO_REGEX, repo_name):
    print(f"Error: {repo_name} is not a valid repository name!")
    sys.exit(1)

if not description:
    description = ""
