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
    
    def test_player_check(self):
        pass

    def test_player_call(self):
        pass

    def test_player_fold(self):
        pass

    def test_player_bet(self):
        pass

    def test_player_go_all_in(self):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
	unittest.main()