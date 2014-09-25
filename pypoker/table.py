'''
This module defines a class for the Poker Table for the game engine
'''

from game import Game
from player import Player

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
		self.current_player = -1

		if min_players < 2:
			raise Exception('Parameter [min_players] must be a postive integer of a minimum value of 2.')
		elif max_players > 10:
			raise Exception('Parameter [max_players] must be a positive integer less than or equal to 10.')
		elif min_players > max_players:
			 raise Exception('Parameter [min_players] must be less than or equal to [maxPlayers].')


	def __str__(self):
		return 'Table has small blind ' + str(self.small_blind) + ', big blind ' \
		+ str(self.big_blind) + ', minimum buy in ' + str(self.min_buy_in) + \
		', and maximum buy in ' + str(self.max_buy_in)

	def start_game(self):
		'''
		Function to start a poker game after table has been initalized and
		players have been added to the table
		'''
		if not self.game:
			self.game = Game(self.small_blind, self.big_blind)
			self.new_round()

	def new_round(self):
		'''
		Function to start a new round in a game
		'''
		pass

	def add_player(self, player_name, chips):
		'''
		Function to add a player to a game
		'''
		if self.min_buy_in <= chips <= self.max_buy_in:
			player = Player(player_name, chips, self)
			self.players_to_add.append(player)

		if self.auto_start and len(self.player) == 0 and len(self.players_to_add) >= self.min_players:
			self.start_game()

	def remove_player(self, player_name):
		'''
		Function to remove a player from a game
		'''
		for index, player in enumerate(self.players):
			if player.player_name == player_name:
				self.players_to_remove.append(index)
				player.fold()

		for index, player in enumerate(self.players):
			if player.player_name == player_name:
				self.players_to_add.pop(index) # need to find equivalent of javascript splice method




