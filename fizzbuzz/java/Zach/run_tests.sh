#!/bin/bash

TEST_PASSED=0
TEST_FAILED=0
SUC_PASS=1

echo "Testing Fizz"
EXPECTED_OUTPUT1="Fizz"
javac zjFizzBuzz.java
ACTUAL_OUTPUT1=$(java zjFizzBuzz 3 3)

if [ "$EXPECTED_OUTPUT1" == "$ACTUAL_OUTPUT1" ]; then
    echo "Test passed"
    TEST_PASSED=$(($TEST_PASSED + $SUC_PASS))
else
    echo "Test failed"
    echo "Expected output:"
    echo "$EXPECTED_OUTPUT1"
    echo "Actual output:"
    echo "$ACTUAL_OUTPUT1"
    TEST_FAILED=$(($TEST_FAILED + $SUC_PASS))
fi

echo " "
echo "Testing Buzz"
EXPECTED_OUTPUT2="Buzz"
javac zjFizzBuzz.java
ACTUAL_OUTPUT2=$(java zjFizzBuzz 5 5)

if [ "$EXPECTED_OUTPUT2" == "$ACTUAL_OUTPUT2" ]; then
    echo "Test passed"
    TEST_PASSED=$(($TEST_PASSED + $SUC_PASS))
else
    echo "Test failed"
    echo "Expected output:"
    echo "$EXPECTED_OUTPUT2"
    echo "Actual output:"
    echo "$ACTUAL_OUTPUT2"
    TEST_FAILED=$(($TEST_FAILED + $SUC_PASS))
fi

echo " "
echo "Testing Ping"
EXPECTED_OUTPUT3="Ping"
javac zjFizzBuzz.java
ACTUAL_OUTPUT3=$(java zjFizzBuzz 7 7)

if [ "$EXPECTED_OUTPUT3" == "$ACTUAL_OUTPUT3" ]; then
    echo "Test passed"
    TEST_PASSED=$(($TEST_PASSED + $SUC_PASS))
else
    echo "Test failed"
    echo "Expected output:"
    echo "$EXPECTED_OUTPUT3"
    echo "Actual output:"
    echo "$ACTUAL_OUTPUT3"
    TEST_FAILED=$(($TEST_FAILED + $SUC_PASS))
fi

echo " "
echo "Testing Pong"
EXPECTED_OUTPUT4="Pong"
javac zjFizzBuzz.java
ACTUAL_OUTPUT4=$(java zjFizzBuzz 11 11)

if [ "$EXPECTED_OUTPUT4" == "$ACTUAL_OUTPUT4" ]; then
    echo "Test passed"
    TEST_PASSED=$(($TEST_PASSED + $SUC_PASS))
else
    echo "Test failed"
    echo "Expected output:"
    echo "$EXPECTED_OUTPUT4"
    echo "Actual output:"
    echo "$ACTUAL_OUTPUT4"
    TEST_FAILED=$(($TEST_FAILED + $SUC_PASS))
fi

echo " "
echo "Testing FizzBuzz"
EXPECTED_OUTPUT5="FizzBuzz"
javac zjFizzBuzz.java
ACTUAL_OUTPUT5=$(java zjFizzBuzz 15 15)

if [ "$EXPECTED_OUTPUT5" == "$ACTUAL_OUTPUT5" ]; then
    echo "Test passed"
    TEST_PASSED=$(($TEST_PASSED + $SUC_PASS))
else
    echo "Test failed"
    echo "Expected output:"
    echo "$EXPECTED_OUTPUT5"
    echo "Actual output:"
    echo "$ACTUAL_OUTPUT5"
    TEST_FAILED=$(($TEST_FAILED + $SUC_PASS))
fi

echo " "
echo "Testing FizzPong"
EXPECTED_OUTPUT6="FizzPong"
javac zjFizzBuzz.java
ACTUAL_OUTPUT6=$(java zjFizzBuzz 33 33)

if [ "$EXPECTED_OUTPUT6" == "$ACTUAL_OUTPUT6" ]; then
    echo "Test passed"
    TEST_PASSED=$(($TEST_PASSED + $SUC_PASS))
else
    echo "Test failed"
    echo "Expected output:"
    echo "$EXPECTED_OUTPUT6"
    echo "Actual output:"
    echo "$ACTUAL_OUTPUT6"
    TEST_FAILED=$(($TEST_FAILED + $SUC_PASS))
fi

echo " "
echo "Testing FizzPing"
EXPECTED_OUTPUT7="FizzPing"
javac zjFizzBuzz.java
ACTUAL_OUTPUT7=$(java zjFizzBuzz 21 21)

if [ "$EXPECTED_OUTPUT7" == "$ACTUAL_OUTPUT7" ]; then
    echo "Test passed"
    TEST_PASSED=$(($TEST_PASSED + $SUC_PASS))
else
    echo "Test failed"
    echo "Expected output:"
    echo "$EXPECTED_OUTPUT7"
    echo "Actual output:"
    echo "$ACTUAL_OUTPUT7"
    TEST_FAILED=$(($TEST_FAILED + $SUC_PASS))
fi

echo " "
echo "Testing BuzzPing"
EXPECTED_OUTPUT8="BuzzPing"
javac zjFizzBuzz.java
ACTUAL_OUTPUT8=$(java zjFizzBuzz 35 35)

if [ "$EXPECTED_OUTPUT8" == "$ACTUAL_OUTPUT8" ]; then
    echo "Test passed"
    TEST_PASSED=$(($TEST_PASSED + $SUC_PASS))
else
    echo "Test failed"
    echo "Expected output:"
    echo "$EXPECTED_OUTPUT8"
    echo "Actual output:"
    echo "$ACTUAL_OUTPUT8"
    TEST_FAILED=$(($TEST_FAILED + $SUC_PASS))
fi

echo " "
echo "Testing BuzzPong"
EXPECTED_OUTPUT9="BuzzPong"
javac zjFizzBuzz.java
ACTUAL_OUTPUT9=$(java zjFizzBuzz 55 55)

if [ "$EXPECTED_OUTPUT9" == "$ACTUAL_OUTPUT9" ]; then
    echo "Test passed"
    TEST_PASSED=$(($TEST_PASSED + $SUC_PASS))
else
    echo "Test failed"
    echo "Expected output:"
    echo "$EXPECTED_OUTPUT9"
    echo "Actual output:"
    echo "$ACTUAL_OUTPUT9"
    TEST_FAILED=$(($TEST_FAILED + $SUC_PASS))
fi

echo " "
echo "Testing PingPong"
EXPECTED_OUTPUT10="PingPong"
javac zjFizzBuzz.java
ACTUAL_OUTPUT10=$(java zjFizzBuzz 77 77)

if [ "$EXPECTED_OUTPUT10" == "$ACTUAL_OUTPUT10" ]; then
    echo "Test passed"
    TEST_PASSED=$(($TEST_PASSED + $SUC_PASS))
else
    echo "Test failed"
    echo "Expected output:"
    echo "$EXPECTED_OUTPUT10"
    echo "Actual output:"
    echo "$ACTUAL_OUTPUT10"
    TEST_FAILED=$(($TEST_FAILED + $SUC_PASS))
fi

echo " "
echo "Testing BuzzPingPong"
EXPECTED_OUTPUT11="BuzzPingPong"
javac zjFizzBuzz.java
ACTUAL_OUTPUT11=$(java zjFizzBuzz 385 385)

if [ "$EXPECTED_OUTPUT11" == "$ACTUAL_OUTPUT11" ]; then
    echo "Test passed"
    TEST_PASSED=$(($TEST_PASSED + $SUC_PASS))
else
    echo "Test failed"
    echo "Expected output:"
    echo "$EXPECTED_OUTPUT11"
    echo "Actual output:"
    echo "$ACTUAL_OUTPUT11"
    TEST_FAILED=$(($TEST_FAILED + $SUC_PASS))
fi

echo " "
echo "Testing FizzPingPong"
EXPECTED_OUTPUT12="FizzPingPong"
javac zjFizzBuzz.java
ACTUAL_OUTPUT12=$(java zjFizzBuzz 231 231)

if [ "$EXPECTED_OUTPUT12" == "$ACTUAL_OUTPUT12" ]; then
    echo "Test passed"
    TEST_PASSED=$(($TEST_PASSED + $SUC_PASS))
else
    echo "Test failed"
    echo "Expected output:"
    echo "$EXPECTED_OUTPUT12"
    echo "Actual output:"
    echo "$ACTUAL_OUTPUT12"
    TEST_FAILED=$(($TEST_FAILED + $SUC_PASS))
fi

echo " "
echo "Testing FizzBuzzPong"
EXPECTED_OUTPUT13="FizzBuzzPong"
javac zjFizzBuzz.java
ACTUAL_OUTPUT13=$(java zjFizzBuzz 165 165)

if [ "$EXPECTED_OUTPUT13" == "$ACTUAL_OUTPUT13" ]; then
    echo "Test passed"
    TEST_PASSED=$(($TEST_PASSED + $SUC_PASS))
else
    echo "Test failed"
    echo "Expected output:"
    echo "$EXPECTED_OUTPUT13"
    echo "Actual output:"
    echo "$ACTUAL_OUTPUT13"
    TEST_FAILED=$(($TEST_FAILED + $SUC_PASS))
fi

echo " "
echo "Testing FizzBuzzPing"
EXPECTED_OUTPUT14="FizzBuzzPing"
javac zjFizzBuzz.java
ACTUAL_OUTPUT14=$(java zjFizzBuzz 105 105)

if [ "$EXPECTED_OUTPUT14" == "$ACTUAL_OUTPUT14" ]; then
    echo "Test passed"
    TEST_PASSED=$(($TEST_PASSED + $SUC_PASS))
else
    echo "Test failed"
    echo "Expected output:"
    echo "$EXPECTED_OUTPUT14"
    echo "Actual output:"
    echo "$ACTUAL_OUTPUT14"
    TEST_FAILED=$(($TEST_FAILED + $SUC_PASS))
fi

echo " "
echo "Testing FizzBuzzPingPong"
EXPECTED_OUTPUT15="FizzBuzzPingPong"
javac zjFizzBuzz.java
ACTUAL_OUTPUT15=$(java zjFizzBuzz 1155 1155)

if [ "$EXPECTED_OUTPUT15" == "$ACTUAL_OUTPUT15" ]; then
    echo "Test passed"
    TEST_PASSED=$(($TEST_PASSED + $SUC_PASS))
else
    echo "Test failed"
    echo "Expected output:"
    echo "$EXPECTED_OUTPUT15"
    echo "Actual output:"
    echo "$ACTUAL_OUTPUT15"
    TEST_FAILED=$(($TEST_FAILED + $SUC_PASS))
fi

echo " "
echo "----------------------------------------"
echo "$TEST_PASSED Test Passed!"
echo "$TEST_FAILED Test Failed!"