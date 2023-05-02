# write a function that calculates a players handicap over a given number of rounds






def handicap(rounds):
    # rounds is a list of tuples
    # each tuple contains the players score and the course rating
    # handicap = (average score - course rating) * 113 / slope
    # return the players handicap
    pass

# write unit tests for handicap.py
import unittest

class TestHandicap(unittest.TestCase):
    def test_handicap(self):
        self.assertEqual(handicap([(80, 72), (75, 72), (90, 72)]), 1.0)

if __name__ == '__main__':
    unittest.main()

# write a function that calculates the distance between two points
# the function should take two tuples as arguments
# each tuple should contain the x and y coordinates of a point
# the function should return the distance between the two points
# the distance formula is sqrt((x2 - x1)^2 + (y2 - y1)^2)


def distance(p1, p2):
    pass

