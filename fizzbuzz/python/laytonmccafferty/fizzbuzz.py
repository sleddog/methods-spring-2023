import sys
'''
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
    '''
    #Darshan adding to Layton's code

def pingpong(maxnumber):
    count = 1;
    while count <= maxnumber:
        string = ""
        if count % 3 == 0:
            string += "Fizz"
        if count % 5 == 0: #added code for ping pong
            string += "Buzz"
        if count % 7 == 0:
            string += "Ping"
        if count % 11 == 0:
            string += "Pong"
        if string != "":
            print(string)
            count += 1
        else:
            print(count)
            count += 1


if __name__ == '__main__':
    userInput = int(sys.argv[1])
    pingpong(userInput)

