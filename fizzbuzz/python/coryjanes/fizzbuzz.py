import sys


def fizzbuzz(total_count):
    number =  1
    while number <= total_count:            
        #if number is divisble by 3, display 'Fizz'
        if number % 3 == 0:
            sys.stdout.write("Fizz")
            print()
        #if number is divisible by 5, display 'Buzz'
        elif number % 5 == 0:
            sys.stdout.write("Buzz")
            print()
        else:
            print(number)
        
        number += 1

fizzbuzz(int(sys.argv[1]))
