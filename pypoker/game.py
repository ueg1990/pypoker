'''
This module defines a class for a game of poker on the table
'''

from deck import Deck

class Game(object):

	def __init__(self, small_blind, big_blind):
		self.small_blind = small_blind
		self.big_blind = big_blind
		self.pot = 0
		self.round_name = 'Deal' # First round
		self.bet_name = 'bet' # bet, raise, re-rause, cap
		self.bets = []
		self.round_bets = []
		self.deck = Deck()
		self.board = []

	def __str__(self):
		return str(self.small_blind) + " " + str(self.big_blind) + " " +  str(self.pot) +  " " +  str(self.bets)