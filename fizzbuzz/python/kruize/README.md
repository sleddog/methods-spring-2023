Navigate to the folder fizzbuzz\python\kruize
Run the command {chmod +x run.sh}
Run the command {./run.sh #} and replace # with the max number you want it to count to.
When it hits a multiple of 3 it will return Fizz
When it hits a multiple of 5 it will return Buzz
When it hits a multiple of 3 & 5 it will return FizzBuzz


```
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
    ```
