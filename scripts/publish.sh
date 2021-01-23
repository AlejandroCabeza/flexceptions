#!/usr/bin/env bash

SCRIPTS_DIRECTORY="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
REPOSITORY_ROOT_DIRECTORY=$SCRIPTS_DIRECTORY/..

python3.8 -m twine upload $REPOSITORY_ROOT_DIRECTORY/dist/*
