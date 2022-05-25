import unittest
from classes.game import Game
from classes.player import Player
from classes.frame import Frame

#not really sure how to use this

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

if __name__ == '__main__':
    unittest.main()