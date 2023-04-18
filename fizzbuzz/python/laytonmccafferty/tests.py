import unittest
import fizzbuzz
class MyTestCase(unittest.TestCase):

    def test_fizz(self):
        self.assertEqual(fizzbuzz.pingpong(3), "fizz")
    def test_buzz(self):
        self.assertEqual(fizzbuzz.pingpong(5), "buzz")
    def test_ping(self):
        self.assertEqual(fizzbuzz.pingpong(7), "ping")
    def test_pong(self):
        self.assertEqual(fizzbuzz.pingpong(11), "pong")

if __name__ == '__main__':
    unittest.main()
