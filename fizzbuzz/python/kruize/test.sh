#!/bin/bash

echo "RUNNING UNIT TESTS"
echo ""

python3 ./test_fizzbuzz.py

unittest_exit_code=$?
if [ $unittest_exit_code -eq 0 ]; then
    echo ""
    echo "UNIT TESTS PASSED"
else 
    echo ""
    echo "UNIT TESTS FAILED"
    echo "EXITING"
    exit 1
fi