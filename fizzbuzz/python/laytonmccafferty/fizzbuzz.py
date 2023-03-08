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
    userInput = int(input("Enter a maximum number: "))
    fizzbuzz(userInput)
