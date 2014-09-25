import unittest
from pypoker import Player
from pypoker import Table

class PlayerTestCase(unittest.TestCase):
    ''' 
    Tests for the Player class
    '''
    def setUp(self):
        self.player = Player('usman', 1000, None)

    def test_player_initialization(self):
    	self.assertEqual([self.player.player_name, self.player.chips], ['usman', 1000])
    
    def tearDown(self):
        pass

if __name__ == '__main__':
	unittest.main()