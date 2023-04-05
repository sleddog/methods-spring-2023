import sys

def fizzbuzz(number):
    counter =  1
    while counter <= number:
        to_print = ""
        if counter%3 == 0:
            to_print += "Fizz"
        if counter%5 == 0:
            to_print += "Buzz"
        if counter%7 == 0:
            to_print += "Ping"
        if counter%11 == 0:
            to_print += "Pong"
        if to_print != "":
            print(to_print)
        else:
            print(counter)
        counter += 1

#Makes sure there are sufficient arguments given
if len(sys.argv) != 2:
    #print("Incorrect number of arguments given.")
    sys.exit()

fizzbuzz(int(sys.argv[1]))
