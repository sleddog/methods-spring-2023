
def fizzbuzz(total_count):
	number =  1
	while number <= total_count:
		# if number is divisble by 3 and 5, display 'FizzBuzz' 
		print(filter(number))
		number += 1

def filter(number : int) -> str:
	to_print : str = ""
	# if number is divisible by 3, display 'Fizz'
	if number % 3 == 0:
		to_print = to_print + "Fizz"
	# if number is divisible by 5, display 'Buzz'
	if number % 5 == 0:
		to_print = to_print + "Buzz"
	if number % 7 == 0:
		to_print = to_print + "Ping"
	if number % 11 == 0:
		to_print = to_print + "Pong"
	if number % 5 != 0 and number % 3 != 0 and number % 7 != 0 and number % 11 != 0:
		to_print = str(number)
	return to_print


fizzbuzz(int(sys.argv[1]))
