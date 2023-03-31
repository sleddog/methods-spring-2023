import unittest
from fizzbuzz import filter

class TestFizzBuzz(unittest.TestCase):
    def test_three(self):
        self.assertEqual(filter(3), 'Fizz')
    def test_five(self):
        self.assertEqual(filter(5), 'Buzz')
    def test_seven(self):
        self.assertEqual(filter(7), 'Ping')
    def test_eleven(self):
        self.assertEqual(filter(11),'Pong')

if __name__ == "__main__":
    unittest.main()