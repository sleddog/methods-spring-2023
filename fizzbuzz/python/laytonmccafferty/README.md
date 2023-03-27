---------Running Layton's FizzBuzz Program---------

	1. First, navigate to the directory 
/methods-spring-2023/fizzbuzz/python/laytonmccafferty
	2. make sure that you have python installed on your machine
	3. run the script using ./run.sh [insert number here]
	4. file should output something like what is here below


``` actual code

import sys

def fizzbuzz(maxnumber):
    count = 1;
    while count <= maxnumber:
        if (count % 3 == 0) and (count % 5 == 0):
            print("fizzbuzz")
            count += 1
        elif count % 5 == 0:
            print("buzz")
            count += 1
        elif count % 3 == 0:
            print("fizz")
            count += 1
        else:
            print(count)
            count += 1
            
if __name__ == '__main__':  
    userInput = int(sys.argv[1])
    fizzbuzz(userInput)
        
```


```  Expected Output

	
FizzBuzz Program
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz
16
17
fizz
19


```
