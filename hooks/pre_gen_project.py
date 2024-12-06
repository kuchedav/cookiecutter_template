import re
import sys

REPO_REGEX = r"^[a-z][-a-z0-9]+$"

repo_name = "{{ cookiecutter.repo_name }}"

if not re.match(REPO_REGEX, repo_name):
    print(
        f"Error: {repo_name} is not a valid repository name!"
    )
