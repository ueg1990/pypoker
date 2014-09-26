'''
This class defines a class for a deck of cards that will be used in the game engine
'''

import random

class Deck(object):
	'''
	This class creates a deck of cards and returns the deck after shuffling
	the dech using the Fisher-Yates algorithm
	'''

	def __init__(self):
		self.deck = []
		self.deck.append('AS')
		self.deck.append('KS')
		self.deck.append('QS')
		self.deck.append('JS')
		self.deck.append('TS')
		self.deck.append('9S')
		self.deck.append('8S')
		self.deck.append('7S')
		self.deck.append('6S')
		self.deck.append('5S')
		self.deck.append('4S')
		self.deck.append('3S')
		self.deck.append('2S')
		self.deck.append('AH')
		self.deck.append('KH')
		self.deck.append('QH')
		self.deck.append('JH')
		self.deck.append('TH')
		self.deck.append('9H')
		self.deck.append('8H')
		self.deck.append('7H')
		self.deck.append('6H')
		self.deck.append('5H')
		self.deck.append('4H')
		self.deck.append('3H')
		self.deck.append('2H')
		self.deck.append('AD')
		self.deck.append('KD')
		self.deck.append('QD')
		self.deck.append('JD')
		self.deck.append('TD')
		self.deck.append('9D')
		self.deck.append('8D')
		self.deck.append('7D')
		self.deck.append('6D')
		self.deck.append('5D')
		self.deck.append('4D')
		self.deck.append('3D')
		self.deck.append('2D')
		self.deck.append('AC')
		self.deck.append('KC')
		self.deck.append('QC')
		self.deck.append('JC')
		self.deck.append('TC')
		self.deck.append('9C')
		self.deck.append('8C')
		self.deck.append('7C')
		self.deck.append('6C')
		self.deck.append('5C')
		self.deck.append('4C')
		self.deck.append('3C')
		self.deck.append('2C')
		
		self.shuffle()
		
	def shuffle(self):
		'''
		Shuffle the deck array with Fisher-Yates algorithm
		'''

		for card_index in xrange(len(self.deck)):
			random_card_index = random.choice(xrange(card_index + 1))
			self.deck[card_index], self.deck[random_card_index] = self.deck[random_card_index], self.deck[card_index]

	def __str__(self):
		return ' '.join(self.deck)

	def __len__(self):
		return len(self.deck)

	def __iter__(self):
		return iter(self.deck)

	def pop(self):
		return self.deck.pop()
		