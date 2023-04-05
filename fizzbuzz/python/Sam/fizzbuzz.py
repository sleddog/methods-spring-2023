import sys

#used to get the value that should be printed for each number
def getValue(x):
    string = ""

    #divisible by 3
    if x%3 == 0:
        string += "Fizz"

    #divisible by 5
    if x%5 == 0:
        string += "Buzz"
        
    #divisible by 7
    if x%7 == 0:
        string += "Ping"

    #divisible by 11
    if x%11 == 0:
        string += "Pong"

    #returns the correct value
    if len(string) > 0:
        return(string)
    else:
        return(x)


if __name__ == "__main__":
    #makes sure that there is a number given
    if(len(sys.argv) == 2):
        pass
    else:
        print("Please enter a number...")
        sys.exit()

    #gets the number and loops
    num = int(sys.argv[1])
    for x in range(1,num+1):
        print(getValue(x))

