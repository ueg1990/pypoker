import unittest
from pypoker import Game

class GameTestCase(unittest.TestCase):
    ''' 
    Tests for the Game class
    '''
    def setUp(self):
        self.game = Game(50, 100)

    def test_game_initialization(self):
    	self.assertEqual([self.game.small_blind, self.game.big_blind], [50,100])

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
