'''
This module re-implements the poker game engine found on 
https://github.com/yannlombard/node-poker in Python

Author: Usman Ehtesham Gul <uehtesham90@gmail.com>
'''

import json
import random

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


class Player(object):
	'''
	This class creates Player objects to play the game
	'''

	def __init__(self, player_name, chips, table):
		self.player_name = player_name
		self.chips = chips
		self.table = table # Circular reference to allow reference back to parent object
		self.folded = False
		self.allIn = False
		self.talked = False
		self.cards = []
		

def main():
	table = Table(50,100,2,10,100,1000)
	player = Player('usman', 1000, table)
	
if __name__ == "__main__":
    main()



