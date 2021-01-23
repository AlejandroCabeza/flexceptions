#!/usr/bin/env bash

SCRIPTS_DIRECTORY="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
REPOSITORY_ROOT_DIRECTORY=$SCRIPTS_DIRECTORY/..

python3 $REPOSITORY_ROOT_DIRECTORY/setup.py sdist bdist_wheel
