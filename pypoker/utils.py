'''
This module contains a set of helper functions that will be used in the 
implementation of the poker game engie
'''

def get_max_bet(list_of_bets):
	'''
	Return the biggest value among the bets
	'''
	return max(list_of_bets)

def check_for_end_of_round(table):
	'''
	Function checks if the current round has ended
	'''
	end_of_round = True
	max_bet = get_max_bet(table.game.bets)
	for index, player in enumerate(table.players):
		if not player.folded:
			if (not player.talked) or (table.game.bets[index] != max_bet):
				if not player.all_in:
					table.current_player = index
					end_of_round = False
	return end_of_round
