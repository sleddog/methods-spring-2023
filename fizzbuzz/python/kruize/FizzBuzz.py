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