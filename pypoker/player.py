'''
This module defines a class for a Player who will play poker in the game engine
'''

from utils import get_player_index, progress, get_max_bet

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
			# Attempt to progress the game
			progress(self.table)
		else:
			print 'Check not allowed, replay please'

	def fold(self):
		'''
		Function to allow player to fold
		'''
		for index, player in enumerate(self.table.players):
			if self == player:
				if self.table.game.bets[index]:
					bet = self.table.game.bets[index]
				else:
					bet = 0
				self.table.game.bets[index] = 0
				self.table.game.pot += bet
				self.talked = True

		# Mark the player as folded
		self.folded = True
		self.turn_bet = {'action': 'fold', 'player_name': self.player_name}
		# Attempt to progress the game
		progress(self.table)


	def bet(self,amount):
		'''
		Function to allow player to place a bet of a given amount
		'''
		if self.chips > amount:
			for index,player in enumerate(self.table.players):
				if self == player:
					self.table.game.bets[index] += amount
					player.chips -= amount
					self.talked = True

			self.turn_bet = {'action': 'bet', 'player_name': self.player_name, 'amount' : amount}
			# Attemp to progress the game
			progress(self.table)
		else:
			print 'You don\'t have enough chips --> ALL IN !!!'
			self.all_in()

	def call(self):
		'''
		Function to allow player to call
		'''
		max_bet = get_max_bet
		if self.chips > max_bet:
			# Match the highest bet
			for index, player in enumerate(self.table.players):
				if self == player:
					if self.table.game.bets[index] >= 0:
						self.chips += self.table.game.bets[index]
					self.chips -= max_bet
					self.table.game.bets[index] = max_bet
					self.talked = True
			self.turn_bet = {'action': 'call', 'player_name': self.player_name, 'amount' : max_bet}
			# Attempt to progress the game
			progress(self.table)
		else:
			print 'You don\'t have enough chips --> ALL IN !!!'
			self.all_in()

	def all_in(self):
		'''
		Function to allow player to go all in
		'''
		for index, player in enumerate(self.table.players):
			if self == player:
				if player.chips != 0:
					all_in_value = player.chips
					self.table.game.bets[index] += player.chips
					player.chips = 0
					self.all_in = True
					self.talked = True
		self.turn_bet = {'action': 'all_in', 'player_name': self.player_name, 'amount' : all_in_value}
		# Attempt to progress the game
		progress(self.table)



