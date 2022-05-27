import unittest
from bowling import Game
from player import Player
from frame import Frame

#not really sure how to use this

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

if __name__ == '__main__':
    unittest.main()