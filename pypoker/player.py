'''
This module defines a class for a Player who will play poker in the game engine
'''

from utils import get_player_index, progress

class Player(object):
	'''
	This class creates Player objects to play the game
	'''

	def __init__(self, player_name, chips, table):
		self.player_name = player_name
		self.chips = chips
		self.table = table # Circular reference to allow reference back to parent object
		self.folded = False
		self.all_in = False
		self.talked = False
		self.cards = []

	def __str__(self):
		return self.player_name + " has " + str(self.chips) + " chips"

	def __eq__(self, other):
		return self.player_name == other.player_name and self.chips == other.chips and self.table == other.table
	
	def check(self):
		'''
		Function to allow player to check
		'''
		check_allow = True
		player_index = get_player_index(self)
		player_bet = self.table.game.bets[player_index]

		for bet in self.table.game.bets:
			if bet > player_bet:
				check_allow = False

		if check_allow:
			self.talked = True
			self.turn_bet = {'action': 'check', 'player_name': self.player_name}
			progress(self.table)
		else:
			print 'Check not allowed, replay please'

	def fold(self):
		'''
		Function to allow player to fold
		'''
		pass

	def bet(self,amount):
		'''
		Function to allow player to place a bet of a given amount
		'''
		pass

	def call(self):
		'''
		Function to allow player to call
		'''
		pass

	def all_in(self):
		'''
		Function to allow player to go al in
		'''
		pass


