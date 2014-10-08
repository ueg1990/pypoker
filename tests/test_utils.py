import unittest
from pypoker import utils, Table, Player

class UtilsTestCase(unittest.TestCase):
    ''' 
    Tests for the utils module
    '''
    def setUp(self):
        self.table = Table(50,100,2,10,100,1000)
        self.player_0 = Player('ue', 1000, self.table)
        self.player_1 = Player('usman', 1000, self.table)
        self.player_2 = Player('ehtesham', 1000, self.table)
        self.player_3 = Player('gul', 1000, self.table)
        self.table.players = [self.player_0 ,self.player_1, self.player_2, self.player_3]

    def test_get_max_bet(self):
    	self.assertEqual(utils.get_max_bet([100, 20,15,101, 30, 19]), 101)

    def test_rank_kickers(self):
    	self.assertEqual(utils.rank_kickers('AAAA', 4), 0.8192)

    def test_rank_comparator(self):
        self.assertEqual(utils.rank_comparator(10, 23), 13)

    def test_get_player_index(self):
    	index = utils.get_player_index(Player('ehtesham', 1000, self.table))
        self.assertEqual(index, 2)

    def test_check_for_winner(self):
        pass

    def test_check_for_end_of_round(self):
        self.table.start_game()
        self.table.players[1].call()
        self.table.players[2].call()
        self.table.players[3].call()
        self.table.players[0].call()

        self.table.players[1].call()
        self.table.players[2].call()
        self.table.players[3].call()
        self.table.players[0].call()
        
        self.table.players[1].call()
        self.table.players[2].call()
        self.table.players[3].call()
        self.table.players[0].call()
        
        self.table.players[1].call()
        self.table.players[2].call()
        self.table.players[3].call()
        self.table.players[0].call()
        
        self.assertTrue(utils.check_for_end_of_round(self.table))
        


    def test_check_for_all_in_players(self):
        pass

    def test_check_for_bankrupt(self):
        pass

    def test_progress(self):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
