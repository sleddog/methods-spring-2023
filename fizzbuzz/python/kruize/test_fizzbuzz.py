import unittest
from FizzBuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(3), 'Fizz')
        self.assertEqual(fizzbuzz(5), 'Buzz')
        self.assertEqual(fizzbuzz(7), 'Ping')
        self.assertEqual(fizzbuzz(11), 'Pong')

if __name__ == '__main__':
    unittest.main()