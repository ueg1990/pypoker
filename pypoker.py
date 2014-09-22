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

def main():
	table = Table(50,100,2,10,100,1000)
	player = Player('usman', 1000, table)
	deck = Deck()
	
if __name__ == "__main__":
    main()



