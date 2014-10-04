'''
This module defines a class to store a given hand
'''

class Hand(object):

	def __init__(self, cards):
		self.cards = cards

	def __str__(self):
		return str(self.cards)

	def __len__(self):
		return len(self.cards)

	def __iter__(self):
		return iter(self.cards)