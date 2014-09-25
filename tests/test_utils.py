import unittest
from pypoker import utils, Table, Player

class UtilsTestCase(unittest.TestCase):
    ''' 
    Tests for the utils module
    '''
    def setUp(self):
        self.table = Table(50,100,2,10,100,1000)
        self.player_1 = Player('usman', 1000, self.table)
        self.player_2 = Player('ehtesham', 1000, self.table)
        self.player_3 = Player('gul', 1000, self.table)
        self.table.players = [self.player_1, self.player_2, self.player_3]

    def test_get_max_bet(self):
    	self.assertEqual(utils.get_max_bet([100, 20,15,101, 30, 19]), 101)

    def test_rank_kickers(self):
    	self.assertEqual(utils.rank_kickers('AAAA', 4), 0.8192)

    def test_rank_comparator(self):
        self.assertEqual(utils.rank_comparator(10, 23), 13)

    def test_get_player_index(self):
    	index = utils.get_player_index(Player('ehtesham', 1000, self.table))
    	self.assertEqual(index, 1)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
