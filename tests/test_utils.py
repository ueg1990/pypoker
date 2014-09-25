import unittest
from pypoker import utils, Table, Player

class UtilsTestCase(unittest.TestCase):
    ''' 
    Tests for the utils module
    '''
    def setUp(self):
        self.table = Table(50,100,2,10,100,1000)

    def test_get_max_bet(self):
    	self.assertEqual(utils.get_max_bet([100, 20,15,101, 30, 19]), 101)

    def test_rank_kickers(self):
    	self.assertEqual(utils.rank_kickers('AAAA', 4), 0.8192)

    def test_rank_comparator(self):
        self.assertEqual(utils.rank_comparator(10, 23), 13)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
