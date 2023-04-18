# write a program that prints the numbers from 1 to n
# for multiples of three print "Fizz" instead of the number
# for multiples of five print "Buzz" instead of the number
# for numbers which are multiples of both three and five print "FizzBuzz" instead of the number

def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

fizzbuzz(100)

# write unit tests for fizzbuzz.py
import unittest

class TestFizzBuzz(unittest.TestCase):
    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), 'FizzBuzz')
        self.assertEqual(fizzbuzz(3), 'Fizz')
        self.assertEqual(fizzbuzz(5), 'Buzz')
        self.assertEqual(fizzbuzz(2), 2)

if __name__ == '__main__':
    unittest.main()
