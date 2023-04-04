
# FizzBuzz++ in Python

Fizzbuzz++ is a simple programming problem where you print out every number up to n, with the caveat that if a number is divisible by 3 you print the word Fizz, by 5 you print Buzz, by 7 you print Ping, and by 11 you print Pong. This solution is written in Python


## Documentation

```python
import sys

def fizzbuzz(n):
    out = ''
    if (n % 3 == 0):                      # If the number is a multiple of 3, it will print Fizz
        out += 'Fizz'
    if (n % 5 == 0):                      # If the number is a multiple of 5, it will print Buzz
        out += 'Buzz'
    if (n % 7 == 0):                      # If the number is a multiple of 7, it will print Ping
        out += 'Ping'
    if (n % 11 == 0):                     # If the number is a multiple of 11, it will print Pong
        out += 'Pong'
    if (out == ''):                       # if out is still empty then it will print the number
        out = str(n)

    return out

def main():
    myInput = int(sys.argv[1])                # Gets the input from the command line
    n = 1
    while n < (myInput+1):
        print(fizzbuzz(n))
        n += 1

if __name__ == '__main__':
    main()
```
The above code is the solution to this problem in Python. The main function simply checks for an input, then loops from 1 to that number. Inside this loop, the fizzbuzz function is called for each number in the loop.

The fizzbuzz function is where the actual calculations come in. The most important part of this function is the use of the modulo or % operator. This operator essentially outputs the remainder if you were to divide the two numbers. If the output is a 0, that means the first number is divisible by the second number. This was used with if statements to check if the number is divisible by 3, 5, 7, or 11.Then, depending on what the number is divisible by, the strings Fizz, Buzz, Ping, and Pong can be added to the output string.

## Instructions

In the root of the git repository run:

```bash
  cd fizzbuzz/python/kruize
```

**Note:** You may have to run either [dos2unix or unix2dos](https://www.geeksforgeeks.org/dos2unix-unix2dos-commands/) if you are having problems with line endings on your system.

Run the test script to unit test the fizzbuzz function:

```bash
  ./test.sh
```

Run the program with a number passed in:

```bash
  ./run.sh 20
```

And you are done!
