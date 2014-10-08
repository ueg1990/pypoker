import unittest
from pypoker import Player
from pypoker import Table

class PlayerTestCase(unittest.TestCase):
    ''' 
    Tests for the Player class
    '''
    def setUp(self):
        self.player = Player('usman', 1000, None)
        self.table = Table(50,100,2,10,100,1000)
        self.table.add_player('bob',1000)
        self.table.add_player('jane',1000)
        self.table.add_player('dylan',1000)
        self.table.add_player('john',1000)
        self.table.start_game()

    def test_player_initialization(self):
    	self.assertEqual([self.player.player_name, self.player.chips], ['usman', 1000])
    
    def test_player_check(self):
        self.table.players[1].call()
        self.table.players[2].call()
        self.table.players[3].call()
        self.table.players[0].call()
        self.table.players[1].check()
        self.assertEqual(self.table.players[1].chips, 900)


    def test_player_call(self):
        self.table.players[1].call()
        self.assertEqual(self.table.players[1].chips, 900)


    def test_player_fold(self):
        self.table.players[1].call()
        self.table.players[2].call()
        self.table.players[3].call()
        self.table.players[0].call()
        self.table.players[1].fold()
        self.assertTrue(self.table.players[1].folded)

    def test_player_bet(self):
        self.table.players[1].call()
        self.table.players[2].call()
        self.table.players[3].call()
        self.table.players[0].call()
        current_chips = self.table.players[1].chips
        self.table.players[1].bet(50)
        self.assertEqual(self.table.players[1].chips + 50, current_chips)

    def test_player_go_all_in(self):
        self.table.players[1].call()
        self.table.players[2].call()
        self.table.players[3].call()
        self.table.players[0].call()
        self.table.players[1].go_all_in()
        self.assertEqual(self.table.players[1].chips, 0)

    def tearDown(self):
        pass

if __name__ == '__main__':
	unittest.main()