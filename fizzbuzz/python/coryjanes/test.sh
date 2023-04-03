#!/bin/bash

echo "RUNNING UNIT TESTS FOR FIZZBUZZ++"
echo ""

python3 ./fizzbuzz_tests.py

unittest_exit_code=$?
if [ $unittest_exit_code -eq 0 ]; then
    echo ""
    echo "UNIT TEST PASSED"
else 
    echo ""
    echo "UNIT TEST FAILED"
    echo "EXITING"
    exit 1
fi