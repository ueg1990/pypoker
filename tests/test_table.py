import unittest
from pypoker import Table, Player, Game

class TableTestCase(unittest.TestCase):
    ''' 
    Tests for the Table class
    '''
    def setUp(self):
        self.table = Table(50, 100, 2, 10, 100, 1000)

    def test_table_initialization(self):
    	self.assertEqual([self.table.small_blind, self.table.big_blind, self.table.min_players,
    	self.table.max_players, self.table.min_buy_in, self.table.max_buy_in], [50, 100, 2, 10, 100, 1000])
    
    def test_table_add_player(self):
        self.table.add_player('usman', 1000)
        self.table.add_player('ehtesham', 1000)
        self.assertEqual(self.table.players_to_add, [Player('usman', 1000, self.table), Player('ehtesham', 1000, self.table)])

    def test_table_remove_player(self):
        self.table.add_player('usman', 1000)
        self.table.add_player('ehtesham', 1000)
        self.table.add_player('gul', 1000)
        self.table.start_game()
        self.table.remove_player('ehtesham')
        
    def test_table_start_game(self):
        self.table.add_player('usman', 1000)
        self.table.add_player('ehtesham', 1000)
        self.table.add_player('gul', 1000)
        self.table.start_game()
        self.assertEqual(self.table.current_player, 0)


    def test_table_new_round(self):
        self.table.add_player('usman', 1000)
        self.table.add_player('ehtesham', 1000)
        self.table.add_player('gul', 1000)
        self.table.game = Game(self.table.small_blind, self.table.big_blind)
        self.table.new_round()
        self.assertEqual(self.table.current_player, 0)

    def tearDown(self):
        pass

if __name__ == '__main__':
	unittest.main()