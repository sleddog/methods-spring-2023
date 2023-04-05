#!/bin/bash

echo "Testing FizzBuzz"
echo "‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾"

python ./fizzbuzz_test.py 

EXIT_STATUS=$?

if [ $EXIT_STATUS -eq 0 ]; then
	echo "Tests passed!"
else
	echo "Tests failed. Exit status: $EXIT_STATUS"
	exit $EXIT_STATUS
fi
