#!/bin/bash
chmod +x run.sh
if [[ "$#" -lt 1 && "$#" -ge 2 ]]
then
  echo "Incorrect number of args supplied" >&2
  exit 1
fi

cargo build

cargo run -- $1