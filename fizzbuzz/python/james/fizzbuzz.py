import sys


def fizzbuzz(number):
    counter =  1
    while counter <= number:
        
        if counter%3 == 0 or counter%5 == 0:
            #divisible by 3 (Fizz)
            if counter%3 == 0:
                sys.stdout.write("Fizz")
            #divisible by 5 (Buzz)
            if counter%5 == 0:
                sys.stdout.write("Buzz")
            print()
        else:
            print(counter)
            
        counter += 1

#Makes sure there are sufficient arguments given
if len(sys.argv) != 2:
    print("Incorrect number of arguments given.")
    sys.exit()

fizzbuzz(int(sys.argv[1]))
