#!/bin/bash

if ! command -v node &> /dev/null
then
    echo "The command 'node' was not found. Please install nodejs."
    exit
fi

FILE=./main.js
if  [ ! -f "$FILE" ]; then
    echo "You need to compile the program first. Please run ./compileFizzbuzz.sh"
    exit
fi

if [ -z "$1" ]
  then
    echo "No number supplied defaulting to 25..."
    num="25"
fi

echo ""

node main.js $1
