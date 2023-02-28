import sys

myInput = int(sys.argv[1])
n = 1

while n < (myInput+1):                      #runs the loop till it gets to your number
    if ((n % 3 == 0) and (n % 5 == 0)):     #gets both conditionals 
        print ('FizzBuzz')
    elif (n % 5 == 0):                      #gets just multiple of 5
        print ('Buzz')
    elif (n % 3 == 0):                      #gets multiple of 3
        print ('Fizz')
    else:                                   #just prints the numbers that don't meet a conditional 
        print (n)

        
    n += 1                                  #increases the number each time in the while loop

