import unittest
from comments import *

class Comments(unittest.TestCase):
    def empty_fulfilmentText(self):
        """Don't let users post empty comments"""

    def upvote(self):
        """Score increases by 1 after upvote method"""

    def downvote(self):
        """Score decreases by 1 after downvote method"""

if __name__ == '__main__':
    unittest.main()
