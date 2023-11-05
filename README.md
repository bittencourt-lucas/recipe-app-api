# recipe-app-api

Project created following the Udemy course "Build a Backend REST API with Python & Django - Advanced".

## How to run the app

### Building the project

`docker-compose build`

### Running the project

`docker-compose up`

## Development information

### Running the linter

`docker-compose run --rm app sh -c "flake8"`

### Running Django commands through the container

`docker-compose run --rm app sh -c "django-admin <command>"`

*e.g. `docker compose run --rm app sh -c "django-admin startproject app ."` creates a new project*