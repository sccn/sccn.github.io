#!/bin/bash

DIRECTORY="/path/to/directory"

if [ -d "$DIRECTORY" ]; then
    # Directory exists, pull changes
    cd "$DIRECTORY"
    git pull
else
    # Directory doesn't exist, clone from GitHub
    git clone https://github.com/username/repository.git "$DIRECTORY"
fi