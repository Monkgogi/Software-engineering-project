# Tiffany

from datetime import datetime

class Comment:
    def __init__(self, userID, text, score=None):
        self.userID = userID
        self.fulfilmentText = text
        self.score = score
        self.time = datetime.now()

    def upvote(self):
        """Upvote comment"""

    def downvote(self):
        """Downvote comment"""

    def remove(self):
        """Remove comment"""

    def make_anon(self):
        """Make comment anonymous"""

    def __repr__(self):
        return str(self.userID)+": "+str(self.fulfilmentText)
