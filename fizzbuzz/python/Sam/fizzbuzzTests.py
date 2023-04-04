import unittest
from fizzbuzz import getValue

class TestFizzbuzz(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(getValue(3), "Fizz")
    def test_buzz(self):
        self.assertEqual(getValue(5), "Buzz")
    def test_ping(self):
        self.assertEqual(getValue(7), "Ping")
    def test_pong(self):
        self.assertEqual(getValue(11),"Pong")
    def test_all(self):
        self.assertEqual(getValue(1155),"FizzBuzzPingPong") 

if __name__ == "__main__":
    unittest.main()
