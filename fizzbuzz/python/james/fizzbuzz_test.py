import unittest
from fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(fizzbuzz(3), 'Fizz')
    def test_buzz(self):
        self.assertEqual(fizzbuzz(5), 'Buzz')
    def test_ping(self):
        self.assertEqual(fizzbuzz(7), 'Ping')
    def test_pong(self):
        self.assertEqual(fizzbuzz(11), 'Pong')
    #def test_fizz_buzz_ping_pong(self):
     #   self.assertEqual(fizzbuzz(1155), 'FizzBuzzPingPong')

if __name__ == '__main__':
    unittest.main()
