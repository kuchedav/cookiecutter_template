FROM python:3.8

RUN mkdir /app
WORKDIR /app/

COPY src/{{ cookiecutter.repo_name }}/. .

ENTRYPOINT ["tail", "-f", "/dev/null"]
