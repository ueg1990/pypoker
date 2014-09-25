import unittest
from pypoker import Hand

class HandTestCase(unittest.TestCase):
    '''
    Tests for the Hand class
    '''
    def setUp(self):
        self.hand = Hand(['AS', 'QS', '2H', 'TD', '7C'])

    def test_hand_of_cards(self):
    	self.assertEqual(list(self.hand), ['AS', 'QS', '2H', 'TD', '7C']) 
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
