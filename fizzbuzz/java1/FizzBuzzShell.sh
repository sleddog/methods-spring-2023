#!/bin/bash

#runs the FizzBuzz code
java zjFizzBuzz.java $1

#prevents shell from closing upon code completion
trap 'sleep infinity' EXIT
echo "CTRL+C to exit shell"