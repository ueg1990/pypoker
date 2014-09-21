'''
This module re-implements the poker game engine found on 
https://github.com/yannlombard/node-poker in Python

Author: Usman Ehtesham Gul <uehtesham90@gmail.com>
'''

class Table(object):
	'''
	Create a Table for a game of poker
	'''

	def __init__(small_blind, big_blind, min_players, max_players, min_buy_in, max_buy_in):
		this.auto_start = False
		this.small_blind = small_blind
		this.big_blind = big_blind
		this.min_players = min_players
		this.max_players = max_players
		this.players = []
		this.dealer = 0
		this.min_buy_in = min_buy_in
		this.max_buy_in = max_buy_in
		this.players_to_remove = []
		this.players_to_add = []
		this.turn_bet = {}
		this.game_winners = []
		this.game_losers = []

		if min_players < 2:
			raise Exception('Parameter [minPlayers] must be a postive integer of a minimum value of 2.')
		elif max_players > 10:
			raise Exception('Parameter [maxPlayers] must be a positive integer less than or equal to 10.')
		elif min_players > max_players:
			 raise Exception('Parameter [minPlayers] must be less than or equal to [maxPlayers].')





