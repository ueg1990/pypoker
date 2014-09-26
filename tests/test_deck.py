import unittest
from pypoker import Deck

class DeckTestCase(unittest.TestCase):
    '''
    Tests for the Deck class
    '''
    def setUp(self):
        self.deck = Deck()

    def test_deck_of_cards(self):
    	deck_of_cards = ['2C', '2D', '2H', '2S', '3C', '3D', '3H', '3S', '4C', 
    	'4D', '4H', '4S', '5C', '5D', '5H', '5S', '6C', '6D', '6H', '6S', '7C',
    	'7D', '7H', '7S', '8C', '8D', '8H', '8S', '9C', '9D', '9H', '9S', 'AC',
    	'AD', 'AH', 'AS', 'JC', 'JD', 'JH', 'JS', 'KC', 'KD', 'KH', 'KS', 'QC',
    	'QD', 'QH', 'QS', 'TC', 'TD', 'TH', 'TS']

    	self.assertEqual(sorted(self.deck), deck_of_cards)

    def test_deck_size(self):
    	self.assertEqual(len(self.deck), 52)

    def test_deck_pop(self):
        self.deck = sorted(self.deck)
        self.assertEqual(self.deck.pop(), 'TS')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
