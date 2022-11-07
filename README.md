## Introduction

Implementation of a simple monopoly game.

## Technologies

 - Python `3.7.9`
 - Docker `3.9`

### Structure

```shell
.
├── monopoly_game
    ├── project
    │   ├── board.py
    │   ├── monopoly.py
    │   ├── player.py
    │   └── property.py
    ├── .gitignore
    ├── docker-compose.yaml
    ├── Dockerfile
    ├── README.md
    ├── requirements.txt
    └── run.py
```

## Running the project

To run the project using docker it is necessary to have `docker` and `docker-compose` installed in your environment.

```shell
# Command to build and execute:
$ docker-compose up

# Only build:
$ docker-compose build
```

To run without docker just use:
(it is needed python `3.7.9` installed on the machine)

```shell
# Command to execute directly:
$ python run.py
```

Results are printed on the terminal.