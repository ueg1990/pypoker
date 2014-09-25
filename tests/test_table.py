import unittest
from pypoker import Table

class TableTestCase(unittest.TestCase):
    ''' 
    Tests for the Table class
    '''
    def setUp(self):
        self.table = Table(50, 100, 2, 10, 100, 1000)

    def test_table_initialization(self):
    	self.assertEqual([self.table.small_blind, self.table.big_blind, self.table.min_players,
    	self.table.max_players, self.table.min_buy_in, self.table.max_buy_in], [50, 100, 2, 10, 100, 1000])
    
    def tearDown(self):
        pass

if __name__ == '__main__':
	unittest.main()