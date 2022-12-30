import re
import sys

REPO_REGEX = r"^[a-z][-a-z0-9]+$"
PACKAGE_REGEX = r"^[_a-z][_a-z0-9]+$"

repo_name = "{{ cookiecutter.repo_name }}"
package_name = "{{ cookiecutter.package_name }}"

if not re.match(REPO_REGEX, repo_name):
    print(
        f"Error: {repo_name} is not a valid repository name!"
    )
elif not re.match(PACKAGE_REGEX, package_name):
    print(
        f"ERROR: {package_name} is not a valid package name"
    )