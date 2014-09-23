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

def check_for_all_in_player(table, winners):
	'''
	Function that returns a list of players that wnet all in
	'''
	all_in_players = []
	for index, winner in enumerate(winners):
		if table.players[winner].all_in:
			all_in_players.append(winner)
	return all_in_players

def check_for_bankrupt(table):
	'''
	Function that checks for players who are out of chips
	'''
	players_not_bankrupt = []
	for index, player in enumerate(table.players):
		if table.players[index].chips <= 0
			table.game_losers.append(table.players[index])
			print 'player ' + table.players[i].player_name + ' is going bankrupt'
		else:
			players_not_bankrupt.append(table.players[index])
	table.players = players_not_bankrupt

def rank_comparator(a,b):
	'''
	Comparator function to be used for sorting
	'''
	return b - a

def rank_kickets(ranks, number_of_cards):
	'''
	Function that returns the total rank value of a given number of cards
	'''
	kicker_rank = 0.0000
	ranks_list = []
	rank = ''

	for index in xrange(len(ranks)):
		rank = ranks[i:i+1]
		if rank == 'A':
			ranks_list.append(0.2048)
		if rank == 'K':
			ranks_list.append(0.1024)
		if rank == 'Q':
			ranks_list.append(0.0512)
		if rank == 'J':
			ranks_list.append(0.0256)
		if rank == 'T':
			ranks_list.append(0.0128)
		if rank == '9':
			ranks_list.append(0.0064)
		if rank == '8':
			ranks_list.append(0.0032)
		if rank == '7':
			ranks_list.append(0.0016)
		if rank == '6':
			ranks_list.append(0.0008)
		if rank == '5':
			ranks_list.append(0.0004)
		if rank == '4':
			ranks_list.append(0.0002)
		if rank == '3':
			ranks_list.append(0.0001)
		if rank == '2':
			ranks_list.append(0.0000)

		ranks_list.sort(rank_comparator)
		# Alternate for loop: sum(ranks_list[item] for item in xrange(number_of_cards))
		for index in xrange(number_of_cards):
			kicker_rank += ranks_list[index]
		return kicker_rank