import unittest
from fizzbuzz import filter

class TestFizzBuzz(unittest.TestCase):
    def test_fizz_buzz(self):
        self.assertEqual(filter(3), 'Fizz')
        self.assertEqual(filter(5), 'Buzz')
        self.assertEqual(filter(7), 'Ping')
        self.assertEqual(filter(11),'Pong')

if __name__ == "__main__":
    unittest.main()