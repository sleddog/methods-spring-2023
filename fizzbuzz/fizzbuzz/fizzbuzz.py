#Import the sys module to access command-line arguments
import sys

def fizz_buzz(number):
    for i in range(1, number+1):
        #If the number is divisible by both 3 and 5, print "FizzBuzz"
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

if __name__ == "__main__":
    #Get the integer input from the command-line
    number = int(sys.argv[1])
    fizz_buzz(number)
