'''
This module defines a class for a Player who will play poker in the game engine
'''

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