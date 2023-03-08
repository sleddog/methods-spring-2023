#!/bin/bash

echo "Please enter an integer: " 
read num

output=$(python fizzbuzz.py $num)

echo -e "$output"
read -p "Press enter to continue..."


