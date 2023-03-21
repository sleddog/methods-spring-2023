import sys

num = int(sys.argv[1])
for x in range(1,num+1):
    if x % 3 == 0:
        if x % 5 == 0:
            print("FizzBuzz")
            continue
        print("Fizz")
        continue
    if x % 5 == 0:
        print("Buzz")
        continue
    print(x)



