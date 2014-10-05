'''
This module defines a class for the Poker Table for the game engine
'''

from game import Game
from player import Player
from deck import Deck

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
		#if not self.game:
		self.game = Game(self.small_blind, self.big_blind)
		self.new_round()

	def new_round(self):
		'''
		Function to start a new round in a game
		'''
		remove_index = 0
		for index, player in enumerate(self.players_to_add):
			if remove_index < len(self.players_to_remove):
				index_player = self.players_to_remove[remove_index]
				self.players[index_player] = self.players_to_add[index]
				remove_index += 1
			else:
				self.players.append(self.players_to_add[index])

		self.players_to_add = []
		self.players_to_remove = []
		self.game_winners = []
		self.game_losers = []

		# Deal 2 cards to each player
		for index, player in enumerate(self.players):
			player.cards.append(self.game.deck.pop())
			player.cards.append(self.game.deck.pop())
			#self.game.bets[index] = 0
			#self.game.round_bets[index] = 0
			self.game.bets.append(0)
			self.game.round_bets.append(0)

		# Identify Small and Big Blind player indexes
		small_blind = self.dealer + 1
		if small_blind >= len(self.players):
			small_blind = 0

		big_blind = self.dealer + 2
		if big_blind >= len(self.players):
			big_blind -= len(self.players)

		# Force blind bets
		self.players[small_blind].chips -= self.small_blind
		self.players[big_blind].chips -= self.big_blind
		self.game.bets[small_blind] = self.small_blind
		self.game.bets[big_blind] = self.big_blind

		# Get current player
		self.current_player = self.dealer + 3
		if self.current_player >= len(self.players):
			self.current_player -= len(self.players)

	def init_new_round(self):
		'''
		Function to initalise next round of current game
		'''
		self.dealer += 1
		if self.dealer >= len(self.players):
			self.dealer = 0

		self.game.pot = 0
		self.game.round_name = 'Deal'
		sef.game.bet_name = 'bet'
		self.game.bets = []
		self.game.deck = Deck()
		self.game.board = []
		for index, player in self.players:
			self.players[index].folded = False
			self.players[index].talked = False
			self.players[index].all_in = False
			self.players[index].cards = []

		self.new_round()


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
				self.players_to_add.pop(index)
