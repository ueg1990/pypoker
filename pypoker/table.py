'''
This module defines a class for the Poker Table for the game engine
'''

class Table(object):
	'''
	Create a Table for a game of poker
	'''

	def __init__(self, small_blind, big_blind, min_players, max_players, min_buy_in, max_buy_in):
		self.auto_start = False
		self.small_blind = small_blind
		self.big_blind = big_blind
		self.min_players = min_players
		self.max_players = max_players
		self.players = []
		self.dealer = 0
		self.min_buy_in = min_buy_in
		self.max_buy_in = max_buy_in
		self.players_to_remove = []
		self.players_to_add = []
		self.turn_bet = {}
		self.game_winners = []
		self.game_losers = []

		if min_players < 2:
			raise Exception('Parameter [minPlayers] must be a postive integer of a minimum value of 2.')
		elif max_players > 10:
			raise Exception('Parameter [maxPlayers] must be a positive integer less than or equal to 10.')
		elif min_players > max_players:
			 raise Exception('Parameter [minPlayers] must be less than or equal to [maxPlayers].')


	def __str__(self):
		return 'Table has small blind ' + str(self.small_blind) + ', big blind ' \
		+ str(self.big_blind) + ', minimum buy in ' + str(self.min_buy_in) + \
		', and maximum buy in ' + str(self.max_buy_in)