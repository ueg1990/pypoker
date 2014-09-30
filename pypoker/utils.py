'''
This module contains a set of helper functions that will be used in the 
implementation of the poker game engie
'''
from hand import Hand
from result import Result

def get_max_bet(list_of_bets):
	'''
	Return the biggest value among the bets
	'''
	return max(list_of_bets)

def check_for_winner(table):
	winners = []
	max_rank = 0.000
	for index,player in enumerate(table.players):
		if player.hand.rank == max_rank and not player.folded:
			winners.append(index)

		if player.hand.rank > max_rank and not player.folded:
			max_rank = player.hand.rank
			winners = []
			winners.append(index)

	part = 0
	prize = 0
	all_in_players = check_for_all_in_players(table, winners)
	if len(all_in_players):
		min_bets = table.game.round_bets[winners[0]]
		for index in xrange(1, len(all_in_players)):
			if table.game.round_bets[winners[index]] != 0 and table.game.round_bets[winners[index]] < min_bets:
				min_bets = table.game.round_bets[winners[index]]
		if min_bets:
			part = min_bets
		else:
			part = 0
	else:
		if table.game.round_bets[winners[0]]:
			part = table.game.round_bets[winners[0]]
		else:
			part = 0

	for index,bet in enumerate(table.game.round_bets):
		if table.game.round_bets[index] > part :
			prize += part
			table.game.round_bets[index] -= part
		else:
			prize += table.game.round_bets[index]
			table.game.round_bets[index] = 0

	for index, winner in enumerate(winners):
		winner_prize = float(prize) / len(winners)
		winning_player = table.players[winner]
		winning_player.chips += winner_prize
		if table.game.round_bets[winners[index]] == 0:
			winning_player.folded = True
			table.game_winners.append({'player_name' : winning_player.player_name, 'amount' : winner_prize,
				'hand' : winning_player.hand, 'chips' : winning_player.chips})
		print 'player ' + table.players[winners[i]].player_name + ' wins !!!'

	round_end = True
	for index, bet in enumerate(table.game.round_bets):
		if bet != 0:
			round_end = False
	if not round_end:
		check_for_winner(table)

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

def check_for_all_in_players(table, winners):
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
		if table.players[index].chips <= 0:
			table.game_losers.append(table.players[index])
			print 'player ' + table.players[i].player_name + ' is going bankrupt'
		else:
			players_not_bankrupt.append(table.players[index])
	table.players = players_not_bankrupt

def get_player_index(player):
	'''
	Function to return index of a given Player object
	'''
	player_index = -1
	for index, item in enumerate(player.table.players):
		if player == player.table.players[index]:
			player_index = index

	return player_index

def progress(table):
	if table.game: 
		if check_for_end_of_round:
			# Move all bets to the pot
			for index,bet in enumerate(table.game.bets):
				if table.game.bets[index]:
					table.game.pot +=  table.game.bets[index]
					table.game.round_bets += table.game.bets[index]

			if table.game.round_name == 'River':
				table.game.round_name = 'Showdown'
				table.game.bets = [] # Need to verify this is equivalent to javacript splice

				# Evaluate each hand
				for index, player in enumerate(table.players):
					cards = table.players[index].cards + table.game.board
					hand = Hand(cards)
					table.players[index].hand = rank_hand(hand)
				check_for_winner(table)
				check_for_bankrupt(table)
				print 'Game Over'

			elif table.game.round_name == 'Turn':
				print 'effective turn'
				table.game.round_name = 'River'
				# Burn a card
				table.game.deck.pop()
				# Turn a card
				table.game.board.append(table.game.deck.pop())

				table.game.bets = [0] * len(table.game.bets)				
				for index in range(len(table.players)):
					table.players[index].talked = False

				print 'deal'
			
			elif table.game.round_name == 'Flop':
				print 'effective flop'
				table.game.round_name = 'Turn'
				table.game.deck.pop()
				# Turn a card
				table.game.board.append(table.game.deck.pop())

				table.game.bets = [0] * len(table.game.bets)				
				for index in range(len(table.players)):
					table.players[index].talked = False

				print 'deal'

			elif table.game.round_name == 'Deal':
				print 'effective deal'
				table.game.round_name = 'Flop'
				table.game.deck.pop()
				# Turn three cards
				for index in xrange(3):
					table.game.board.append(table.game.deck.pop())

				table.game.bets = [0] * len(table.game.bets)				
				for index in range(len(table.players)):
					table.players[index].talked = False

				print 'deal'

			if table.current_player >= len(table.players) - 1:
				table.current_player = 0
			else:
				table.current_player += 1


def rank_comparator(a,b):
	'''
	Comparator function to be used for sorting
	'''
	return b - a

def rank_kickers(ranks, number_of_cards):
	'''
	Function that returns the total rank value of a given number of cards
	'''
	kicker_rank = 0.0000
	ranks_list = []
	rank = ''

	for index in xrange(len(ranks)):
		rank = ranks[index:index+1]
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
	
	ranks_list.sort()
	ranks_list.reverse()
	# Alternate for loop: sum(ranks_list[item] for item in xrange(number_of_cards))
	for index in xrange(number_of_cards):
		kicker_rank += ranks_list[index]
	return kicker_rank

def rank_hand(hand):
	'''
	Function to rank a given hand
	'''
	result = rank_hand_int(hand)
	hand.rank = result.rank
	hand.message = result.message
	return hand

def rank_hands(hands):
	'''
	Function to rank a given list of hands
	'''
	for hand in hands:
		result = rank_hand_int(hand)
		hand.rank = result.rank
		hand.message = result.message
	return hands

def rank_hand_int(hand):
	'''
	Get rank valur of a given hand and return a Result object with appropriate message
	'''
	rank = 0.0000
	message = ''
	hand_ranks = []
	hand_suits = []

	for index, card in enumerate(hand.cards):
		hand_ranks[index] = card[0]
		hand_suits[index] = card[1]

	# Verify the following 3 lines - Very Important!!!
	ranks = ','.join(sorted(hand_ranks)) # Replace non-wirds with ''
	suits = ','.join(sorted(hand_suits)) # Replace non-wirds with ''
	cards = ','.join(hand.cards)

	# Four of a kind
	if rank == 0:
		if ranks.index('AAAA') > -1:
			rank = 292 + rank_kickers(ranks.replace('AAAA',''), 1)

		if ranks.index('KKKK') > -1 and rank == 0:
			rank = 291 + rank_kickers(ranks.replace('KKKK',''), 1)

		if ranks.index('QQQQ') > -1 and rank == 0:
			rank = 290 + rank_kickers(ranks.replace('QQQQ',''), 1)

		if ranks.index('JJJJ') > -1 and rank == 0:
			rank = 289 + rank_kickers(ranks.replace('JJJJ',''), 1)

		if ranks.index('TTTT') > -1 and rank == 0:
			rank = 288 + rank_kickers(ranks.replace('TTTT',''), 1)

		if ranks.index('9999') > -1 and rank == 0:
			rank = 287 + rank_kickers(ranks.replace('9999',''), 1)

		if ranks.index('8888') > -1 and rank == 0:
			rank = 286 + rank_kickers(ranks.replace('8888',''), 1)

		if ranks.index('7777') > -1 and rank == 0:
			rank = 285 + rank_kickers(ranks.replace('7777',''), 1)

		if ranks.index('6666') > -1 and rank == 0:
			rank = 284 + rank_kickers(ranks.replace('6666',''), 1)

		if ranks.index('5555') > -1 and rank == 0:
			rank = 283 + rank_kickers(ranks.replace('5555',''), 1)

		if ranks.index('4444') > -1 and rank == 0:
			rank = 282 + rank_kickers(ranks.replace('4444',''), 1)

		if ranks.index('3333') > -1 and rank == 0:
			rank = 281 + rank_kickers(ranks.replace('3333',''), 1)

		if ranks.index('2222') > -1 and rank == 0:
			rank = 280 + rank_kickers(ranks.replace('2222',''), 1)

		if rank:
			message = 'Four of a kind'

	# Full House
	if rank == 0:
		if ranks.index('AAA') > -1 and ranks.index('KK') > -1:
			rank = 279

		if ranks.index('AAA') > -1 and ranks.index('QQ') > -1 and rank == 0:
			rank = 278

		if ranks.index('AAA') > -1 and ranks.index('JJ') > -1 and rank == 0:
			rank = 277

		if ranks.index('AAA') > -1 and ranks.index('TT') > -1 and rank == 0:
			rank = 276

		if ranks.index('AAA') > -1 and ranks.index('99') > -1 and rank == 0:
			rank = 275

		if ranks.index('AAA') > -1 and ranks.index('88') > -1 and rank == 0:
			rank = 274

		if ranks.index('AAA') > -1 and ranks.index('77') > -1 and rank == 0:
			rank = 273

		if ranks.index('AAA') > -1 and ranks.index('66') > -1 and rank == 0:
			rank = 272

		if ranks.index('AAA') > -1 and ranks.index('55') > -1 and rank == 0:
			rank = 271

		if ranks.index('AAA') > -1 and ranks.index('44') > -1 and rank == 0:
			rank = 270

		if ranks.index('AAA') > -1 and ranks.index('33') > -1 and rank == 0:
			rank = 269

		if ranks.index('AAA') > -1 and ranks.index('22') > -1 and rank == 0:
			rank = 268

		if ranks.index('KKK') > -1 and ranks.index('AA') > -1 and rank == 0:
			rank = 267

		if ranks.index('KKK') > -1 and ranks.index('QQ') > -1 and rank == 0:
			rank = 266

		if ranks.index('KKK') > -1 and ranks.index('JJ') > -1 and rank == 0:
			rank = 265

		if ranks.index('KKK') > -1 and ranks.index('TT') > -1 and rank == 0:
			rank = 264

		if ranks.index('KKK') > -1 and ranks.index('99') > -1 and rank == 0:
			rank = 263

		if ranks.index('KKK') > -1 and ranks.index('88') > -1 and rank == 0:
			rank = 262

		if ranks.index('KKK') > -1 and ranks.index('77') > -1 and rank == 0:
			rank = 261

		if ranks.index('KKK') > -1 and ranks.index('66') > -1 and rank == 0:
			rank = 260

		if ranks.index('KKK') > -1 and ranks.index('55') > -1 and rank == 0:
			rank = 259

		if ranks.index('KKK') > -1 and ranks.index('44') > -1 and rank == 0:
			rank = 258

		if ranks.index('KKK') > -1 and ranks.index('33') > -1 and rank == 0:
			rank = 257

		if ranks.index('KKK') > -1 and ranks.index('22') > -1 and rank == 0:
			rank = 256

		if ranks.index('QQQ') > -1 and ranks.index('AA') > -1 and rank == 0:
			rank = 255

		if ranks.index('QQQ') > -1 and ranks.index('KK') > -1 and rank == 0:
			rank = 254

		if ranks.index('QQQ') > -1 and ranks.index('JJ') > -1 and rank == 0:
			rank = 253

		if ranks.index('QQQ') > -1 and ranks.index('TT') > -1 and rank == 0:
			rank = 252

		if ranks.index('QQQ') > -1 and ranks.index('99') > -1 and rank == 0:
			rank = 251

		if ranks.index('QQQ') > -1 and ranks.index('88') > -1 and rank == 0:
			rank = 250

		if ranks.index('QQQ') > -1 and ranks.index('77') > -1 and rank == 0:
			rank = 249

		if ranks.index('QQQ') > -1 and ranks.index('66') > -1 and rank == 0:
			rank = 248

		if ranks.index('QQQ') > -1 and ranks.index('55') > -1 and rank == 0:
			rank = 247

		if ranks.index('QQQ') > -1 and ranks.index('44') > -1 and rank == 0:
			rank = 246

		if ranks.index('QQQ') > -1 and ranks.index('33') > -1 and rank == 0:
			rank = 245

		if ranks.index('QQQ') > -1 and ranks.index('22') > -1 and rank == 0:
			rank = 244

		if ranks.index('JJJ') > -1 and ranks.index('AA') > -1 and rank == 0:
			rank = 243

		if ranks.index('JJJ') > -1 and ranks.index('KK') > -1 and rank == 0:
			rank = 242

		if ranks.index('JJJ') > -1 and ranks.index('QQ') > -1 and rank == 0:
			rank = 241

		if ranks.index('JJJ') > -1 and ranks.index('TT') > -1 and rank == 0:
			rank = 240

		if ranks.index('JJJ') > -1 and ranks.index('99') > -1 and rank == 0:
			rank = 239

		if ranks.index('JJJ') > -1 and ranks.index('88') > -1 and rank == 0:
			rank = 238

		if ranks.index('JJJ') > -1 and ranks.index('77') > -1 and rank == 0:
			rank = 237

		if ranks.index('JJJ') > -1 and ranks.index('66') > -1 and rank == 0:
			rank = 236

		if ranks.index('JJJ') > -1 and ranks.index('55') > -1 and rank == 0:
			rank = 235

		if ranks.index('JJJ') > -1 and ranks.index('44') > -1 and rank == 0:
			rank = 234

		if ranks.index('JJJ') > -1 and ranks.index('33') > -1 and rank == 0:
			rank = 233

		if ranks.index('JJJ') > -1 and ranks.index('22') > -1 and rank == 0:
			rank = 232

		if ranks.index('TTT') > -1 and ranks.index('AA') > -1 and rank == 0:
			rank = 231

		if ranks.index('TTT') > -1 and ranks.index('KK') > -1 and rank == 0:
			rank = 230

		if ranks.index('TTT') > -1 and ranks.index('QQ') > -1 and rank == 0:
			rank = 229

		if ranks.index('TTT') > -1 and ranks.index('JJ') > -1 and rank == 0:
			rank = 228

		if ranks.index('TTT') > -1 and ranks.index('99') > -1 and rank == 0:
			rank = 227

		if ranks.index('TTT') > -1 and ranks.index('88') > -1 and rank == 0:
			rank = 226

		if ranks.index('TTT') > -1 and ranks.index('77') > -1 and rank == 0:
			rank = 225

		if ranks.index('TTT') > -1 and ranks.index('66') > -1 and rank == 0:
			rank = 224

		if ranks.index('TTT') > -1 and ranks.index('55') > -1 and rank == 0:
			rank = 223

		if ranks.index('TTT') > -1 and ranks.index('44') > -1 and rank == 0:
			rank = 222

		if ranks.index('TTT') > -1 and ranks.index('33') > -1 and rank == 0:
			rank = 221

		if ranks.index('TTT') > -1 and ranks.index('22') > -1 and rank == 0:
			rank = 220

		if ranks.index('999') > -1 and ranks.index('AA') > -1 and rank == 0:
			rank = 219

		if ranks.index('999') > -1 and ranks.index('KK') > -1 and rank == 0:
			rank = 218

		if ranks.index('999') > -1 and ranks.index('QQ') > -1 and rank == 0:
			rank = 217

		if ranks.index('999') > -1 and ranks.index('JJ') > -1 and rank == 0:
			rank = 216

		if ranks.index('999') > -1 and ranks.index('TT') > -1 and rank == 0:
			rank = 215

		if ranks.index('999') > -1 and ranks.index('88') > -1 and rank == 0:
			rank = 214

		if ranks.index('999') > -1 and ranks.index('77') > -1 and rank == 0:
			rank = 213

		if ranks.index('999') > -1 and ranks.index('66') > -1 and rank == 0:
			rank = 212

		if ranks.index('999') > -1 and ranks.index('55') > -1 and rank == 0:
			rank = 211

		if ranks.index('999') > -1 and ranks.index('44') > -1 and rank == 0:
			rank = 210

		if ranks.index('999') > -1 and ranks.index('33') > -1 and rank == 0:
			rank = 209

		if ranks.index('999') > -1 and ranks.index('22') > -1 and rank == 0:
			rank = 208

		if ranks.index('888') > -1 and ranks.index('AA') > -1 and rank == 0:
			rank = 207

		if ranks.index('888') > -1 and ranks.index('KK') > -1 and rank == 0:
			rank = 206

		if ranks.index('888') > -1 and ranks.index('QQ') > -1 and rank == 0:
			rank = 205

		if ranks.index('888') > -1 and ranks.index('JJ') > -1 and rank == 0:
			rank = 204

		if ranks.index('888') > -1 and ranks.index('TT') > -1 and rank == 0:
			rank = 203

		if ranks.index('888') > -1 and ranks.index('99') > -1 and rank == 0:
			rank = 202

		if ranks.index('888') > -1 and ranks.index('77') > -1 and rank == 0:
			rank = 201

		if ranks.index('888') > -1 and ranks.index('66') > -1 and rank == 0:
			rank = 200

		if ranks.index('888') > -1 and ranks.index('55') > -1 and rank == 0:
			rank = 199

		if ranks.index('888') > -1 and ranks.index('44') > -1 and rank == 0:
			rank = 198

		if ranks.index('888') > -1 and ranks.index('33') > -1 and rank == 0:
			rank = 197

		if ranks.index('888') > -1 and ranks.index('22') > -1 and rank == 0:
			rank = 196

		if ranks.index('777') > -1 and ranks.index('AA') > -1 and rank == 0:
			rank = 195

		if ranks.index('777') > -1 and ranks.index('KK') > -1 and rank == 0:
			rank = 194

		if ranks.index('777') > -1 and ranks.index('QQ') > -1 and rank == 0:
			rank = 193

		if ranks.index('777') > -1 and ranks.index('JJ') > -1 and rank == 0:
			rank = 192

		if ranks.index('777') > -1 and ranks.index('TT') > -1 and rank == 0:
			rank = 191

		if ranks.index('777') > -1 and ranks.index('99') > -1 and rank == 0:
			rank = 190

		if ranks.index('777') > -1 and ranks.index('88') > -1 and rank == 0:
			rank = 189

		if ranks.index('777') > -1 and ranks.index('66') > -1 and rank == 0:
			rank = 188

		if ranks.index('777') > -1 and ranks.index('55') > -1 and rank == 0:
			rank = 187

		if ranks.index('777') > -1 and ranks.index('44') > -1 and rank == 0:
			rank = 186

		if ranks.index('777') > -1 and ranks.index('33') > -1 and rank == 0:
			rank = 185

		if ranks.index('777') > -1 and ranks.index('22') > -1 and rank == 0:
			rank = 184

		if ranks.index('666') > -1 and ranks.index('AA') > -1 and rank == 0:
			rank = 183

		if ranks.index('666') > -1 and ranks.index('KK') > -1 and rank == 0:
			rank = 182

		if ranks.index('666') > -1 and ranks.index('QQ') > -1 and rank == 0:
			rank = 181

		if ranks.index('666') > -1 and ranks.index('JJ') > -1 and rank == 0:
			rank = 180

		if ranks.index('666') > -1 and ranks.index('TT') > -1 and rank == 0:
			rank = 179

		if ranks.index('666') > -1 and ranks.index('99') > -1 and rank == 0:
			rank = 178

		if ranks.index('666') > -1 and ranks.index('88') > -1 and rank == 0:
			rank = 177

		if ranks.index('666') > -1 and ranks.index('77') > -1 and rank == 0:
			rank = 176

		if ranks.index('666') > -1 and ranks.index('55') > -1 and rank == 0:
			rank = 175

		if ranks.index('666') > -1 and ranks.index('44') > -1 and rank == 0:
			rank = 174

		if ranks.index('666') > -1 and ranks.index('33') > -1 and rank == 0:
			rank = 173

		if ranks.index('666') > -1 and ranks.index('22') > -1 and rank == 0:
			rank = 172

		if ranks.index('555') > -1 and ranks.index('AA') > -1 and rank == 0:
			rank = 171

		if ranks.index('555') > -1 and ranks.index('KK') > -1 and rank == 0:
			rank = 170

		if ranks.index('555') > -1 and ranks.index('QQ') > -1 and rank == 0:
			rank = 169

		if ranks.index('555') > -1 and ranks.index('JJ') > -1 and rank == 0:
			rank = 168

		if ranks.index('555') > -1 and ranks.index('TT') > -1 and rank == 0:
			rank = 167

		if ranks.index('555') > -1 and ranks.index('99') > -1 and rank == 0:
			rank = 166

		if ranks.index('555') > -1 and ranks.index('88') > -1 and rank == 0:
			rank = 165

		if ranks.index('555') > -1 and ranks.index('77') > -1 and rank == 0:
			rank = 164

		if ranks.index('555') > -1 and ranks.index('66') > -1 and rank == 0:
			rank = 163

		if ranks.index('555') > -1 and ranks.index('44') > -1 and rank == 0:
			rank = 162

		if ranks.index('555') > -1 and ranks.index('33') > -1 and rank == 0:
			rank = 161

		if ranks.index('555') > -1 and ranks.index('22') > -1 and rank == 0:
			rank = 160

		if ranks.index('444') > -1 and ranks.index('AA') > -1 and rank == 0:
			rank = 159

		if ranks.index('444') > -1 and ranks.index('KK') > -1 and rank == 0:
			rank = 158

		if ranks.index('444') > -1 and ranks.index('QQ') > -1 and rank == 0:
			rank = 157

		if ranks.index('444') > -1 and ranks.index('JJ') > -1 and rank == 0:
			rank = 156

		if ranks.index('444') > -1 and ranks.index('TT') > -1 and rank == 0:
			rank = 155

		if ranks.index('444') > -1 and ranks.index('99') > -1 and rank == 0:
			rank = 154

		if ranks.index('444') > -1 and ranks.index('88') > -1 and rank == 0:
			rank = 153

		if ranks.index('444') > -1 and ranks.index('77') > -1 and rank == 0:
			rank = 152

		if ranks.index('444') > -1 and ranks.index('66') > -1 and rank == 0:
			rank = 151

		if ranks.index('444') > -1 and ranks.index('55') > -1 and rank == 0:
			rank = 150

		if ranks.index('444') > -1 and ranks.index('33') > -1 and rank == 0:
			rank = 149

		if ranks.index('444') > -1 and ranks.index('22') > -1 and rank == 0:
			rank = 148

		if ranks.index('333') > -1 and ranks.index('AA') > -1 and rank == 0:
			rank = 147

		if ranks.index('333') > -1 and ranks.index('KK') > -1 and rank == 0:
			rank = 146

		if ranks.index('333') > -1 and ranks.index('QQ') > -1 and rank == 0:
			rank = 145

		if ranks.index('333') > -1 and ranks.index('JJ') > -1 and rank == 0:
			rank = 144

		if ranks.index('333') > -1 and ranks.index('TT') > -1 and rank == 0:
			rank = 143

		if ranks.index('333') > -1 and ranks.index('99') > -1 and rank == 0:
			rank = 142

		if ranks.index('333') > -1 and ranks.index('88') > -1 and rank == 0:
			rank = 141

		if ranks.index('333') > -1 and ranks.index('77') > -1 and rank == 0:
			rank = 140

		if ranks.index('333') > -1 and ranks.index('66') > -1 and rank == 0:
			rank = 139

		if ranks.index('333') > -1 and ranks.index('55') > -1 and rank == 0:
			rank = 138

		if ranks.index('333') > -1 and ranks.index('44') > -1 and rank == 0:
			rank = 137

		if ranks.index('333') > -1 and ranks.index('22') > -1 and rank == 0:
			rank = 136

		if ranks.index('222') > -1 and ranks.index('AA') > -1 and rank == 0:
			rank = 135

		if ranks.index('222') > -1 and ranks.index('KK') > -1 and rank == 0:
			rank = 134

		if ranks.index('222') > -1 and ranks.index('QQ') > -1 and rank == 0:
			rank = 133

		if ranks.index('222') > -1 and ranks.index('JJ') > -1 and rank == 0:
			rank = 132

		if ranks.index('222') > -1 and ranks.index('TT') > -1 and rank == 0:
			rank = 131

		if ranks.index('222') > -1 and ranks.index('99') > -1 and rank == 0:
			rank = 130

		if ranks.index('222') > -1 and ranks.index('88') > -1 and rank == 0:
			rank = 129

		if ranks.index('222') > -1 and ranks.index('77') > -1 and rank == 0:
			rank = 128

		if ranks.index('222') > -1 and ranks.index('66') > -1 and rank == 0:
			rank = 127

		if ranks.index('222') > -1 and ranks.index('55') > -1 and rank == 0:
			rank = 126

		if ranks.index('222') > -1 and ranks.index('44') > -1 and rank == 0:
			rank = 125

		if ranks.index('222') > -1 and ranks.index('33') > -1 and rank == 0:
			rank = 124

		if rank != 0:
			message = 'Full House'

	# Flush 
	if rank == 0:
		if (suits.index('CCCCC') > -1 or suits.index('DDDDD') > -1 or 
		suits.index('HHHHH') > -1 or suits.index('SSSS') > -1): 
			rank = 123
			message = Flush

		# Straight Flush
		if (cards.index('TC') > -1 and cards.index('JC') > -1 and
		cards.index('QC') > -1 and cards.index('KC') > -1 and
		cards.index('AC') > -1 and rank = 123):
		    rank = 302
		    message = 'Straight Flush'

		if (cards.index('TD') > -1 and cards.index('JD') > -1 and
		cards.index('QD') > -1 and cards.index('KD') > -1 and
		cards.index('AD') > -1 and rank = 123):
		    rank = 302
		    message = 'Straight Flush'

		if (cards.index('TH') > -1 and cards.index('JH') > -1 and
		cards.index('QH') > -1 and cards.index('KH') > -1 and
		cards.index('AH') > -1 and rank = 123):
		    rank = 302
		    message = 'Straight Flush'

		if (cards.index('TS') > -1 and cards.index('JS') > -1 and
		cards.index('QS') > -1 and cards.index('KS') > -1 and
		cards.index('AS') > -1 and rank = 123):
		    rank = 302
		    message = 'Straight Flush'

		if (cards.index('9C') > -1 and cards.index('TC') > -1 and
		cards.index('JC') > -1 and cards.index('QC') > -1 and
		cards.index('KC') > -1 and rank = 123):
		    rank = 301
		    message = 'Straight Flush'

		if (cards.index('9D') > -1 and cards.index('TD') > -1 and
		cards.index('JD') > -1 and cards.index('QD') > -1 and
		cards.index('KD') > -1 and rank = 123):
		    rank = 301
		    message = 'Straight Flush'

		if (cards.index('9H') > -1 and cards.index('TH') > -1 and
		cards.index('JH') > -1 and cards.index('QH') > -1 and
		cards.index('KH') > -1 and rank = 123):
		    rank = 301
		    message = 'Straight Flush'

		if (cards.index('9S') > -1 and cards.index('TS') > -1 and
		cards.index('JS') > -1 and cards.index('QS') > -1 and
		cards.index('KS') > -1 and rank = 123):
		    rank = 301
		    message = 'Straight Flush'

		if (cards.index('8C') > -1 and cards.index('9C') > -1 and
		cards.index('TC') > -1 and cards.index('JC') > -1 and
		cards.index('QC') > -1 and rank = 123):
		    rank = 300
		    message = 'Straight Flush'

		if (cards.index('8D') > -1 and cards.index('9D') > -1 and
		cards.index('TD') > -1 and cards.index('JD') > -1 and
		cards.index('QD') > -1 and rank = 123):
		    rank = 300
		    message = 'Straight Flush'

		if (cards.index('8H') > -1 and cards.index('9H') > -1 and
		cards.index('TH') > -1 and cards.index('JH') > -1 and
		cards.index('QH') > -1 and rank = 123):
		    rank = 300
		    message = 'Straight Flush'

		if (cards.index('8S') > -1 and cards.index('9S') > -1 and
		cards.index('TS') > -1 and cards.index('JS') > -1 and
		cards.index('QS') > -1 and rank = 123):
		    rank = 300
		    message = 'Straight Flush'

		if (cards.index('7C') > -1 and cards.index('8C') > -1 and
		cards.index('9C') > -1 and cards.index('TC') > -1 and
		cards.index('JC') > -1 and rank = 123):
		    rank = 299
		    message = 'Straight Flush'

		if (cards.index('7D') > -1 and cards.index('8D') > -1 and
		cards.index('9D') > -1 and cards.index('TD') > -1 and
		cards.index('JD') > -1 and rank = 123):
		    rank = 299
		    message = 'Straight Flush'

		if (cards.index('7H') > -1 and cards.index('8H') > -1 and
		cards.index('9H') > -1 and cards.index('TH') > -1 and
		cards.index('JH') > -1 and rank = 123):
		    rank = 299
		    message = 'Straight Flush'

		if (cards.index('7S') > -1 and cards.index('8S') > -1 and
		cards.index('9S') > -1 and cards.index('TS') > -1 and
		cards.index('JS') > -1 and rank = 123):
		    rank = 299
		    message = 'Straight Flush'

		if (cards.index('6C') > -1 and cards.index('7C') > -1 and
		cards.index('8C') > -1 and cards.index('9C') > -1 and
		cards.index('TC') > -1 and rank = 123):
		    rank = 298
		    message = 'Straight Flush'

		if (cards.index('6D') > -1 and cards.index('7D') > -1 and
		cards.index('8D') > -1 and cards.index('9D') > -1 and
		cards.index('TD') > -1 and rank = 123):
		    rank = 298
		    message = 'Straight Flush'

		if (cards.index('6H') > -1 and cards.index('7H') > -1 and
		cards.index('8H') > -1 and cards.index('9H') > -1 and
		cards.index('TH') > -1 and rank = 123):
		    rank = 298
		    message = 'Straight Flush'

		if (cards.index('6S') > -1 and cards.index('7S') > -1 and
		cards.index('8S') > -1 and cards.index('9S') > -1 and
		cards.index('TS') > -1 and rank = 123):
		    rank = 298
		    message = 'Straight Flush'

		if (cards.index('5C') > -1 and cards.index('6C') > -1 and
		cards.index('7C') > -1 and cards.index('8C') > -1 and
		cards.index('9C') > -1 and rank = 123):
		    rank = 297
		    message = 'Straight Flush'

		if (cards.index('5D') > -1 and cards.index('6D') > -1 and
		cards.index('7D') > -1 and cards.index('8D') > -1 and
		cards.index('9D') > -1 and rank = 123):
		    rank = 297
		    message = 'Straight Flush'

		if (cards.index('5H') > -1 and cards.index('6H') > -1 and
		cards.index('7H') > -1 and cards.index('8H') > -1 and
		cards.index('9H') > -1 and rank = 123):
		    rank = 297
		    message = 'Straight Flush'

		if (cards.index('5S') > -1 and cards.index('6S') > -1 and
		cards.index('7S') > -1 and cards.index('8S') > -1 and
		cards.index('9S') > -1 and rank = 123):
		    rank = 297
		    message = 'Straight Flush'

		if (cards.index('4C') > -1 and cards.index('5C') > -1 and
		cards.index('6C') > -1 and cards.index('7C') > -1 and
		cards.index('8C') > -1 and rank = 123):
		    rank = 296
		    message = 'Straight Flush'

		if (cards.index('4D') > -1 and cards.index('5D') > -1 and
		cards.index('6D') > -1 and cards.index('7D') > -1 and
		cards.index('8D') > -1 and rank = 123):
		    rank = 296
		    message = 'Straight Flush'

		if (cards.index('4H') > -1 and cards.index('5H') > -1 and
		cards.index('6H') > -1 and cards.index('7H') > -1 and
		cards.index('8H') > -1 and rank = 123):
		    rank = 296
		    message = 'Straight Flush'

		if (cards.index('4S') > -1 and cards.index('5S') > -1 and
		cards.index('6S') > -1 and cards.index('7S') > -1 and
		cards.index('8S') > -1 and rank = 123):
		    rank = 296
		    message = 'Straight Flush'

		if (cards.index('3C') > -1 and cards.index('4C') > -1 and
		cards.index('5C') > -1 and cards.index('6C') > -1 and
		cards.index('7C') > -1 and rank = 123):
		    rank = 295
		    message = 'Straight Flush'

		if (cards.index('3D') > -1 and cards.index('4D') > -1 and
		cards.index('5D') > -1 and cards.index('6D') > -1 and
		cards.index('7D') > -1 and rank = 123):
		    rank = 295
		    message = 'Straight Flush'

		if (cards.index('3H') > -1 and cards.index('4H') > -1 and
		cards.index('5H') > -1 and cards.index('6H') > -1 and
		cards.index('7H') > -1 and rank = 123):
		    rank = 295
		    message = 'Straight Flush'

		if (cards.index('3S') > -1 and cards.index('4S') > -1 and
		cards.index('5S') > -1 and cards.index('6S') > -1 and
		cards.index('7S') > -1 and rank = 123):
		    rank = 295
		    message = 'Straight Flush'

		if (cards.index('2C') > -1 and cards.index('3C') > -1 and
		cards.index('4C') > -1 and cards.index('5C') > -1 and
		cards.index('6C') > -1 and rank = 123):
		    rank = 294
		    message = 'Straight Flush'

		if (cards.index('2D') > -1 and cards.index('3D') > -1 and
		cards.index('4D') > -1 and cards.index('5D') > -1 and
		cards.index('6D') > -1 and rank = 123):
		    rank = 294
		    message = 'Straight Flush'

		if (cards.index('2H') > -1 and cards.index('3H') > -1 and
		cards.index('4H') > -1 and cards.index('5H') > -1 and
		cards.index('6H') > -1 and rank = 123):
		    rank = 294
		    message = 'Straight Flush'

		if (cards.index('2S') > -1 and cards.index('3S') > -1 and
		cards.index('4S') > -1 and cards.index('5S') > -1 and
		cards.index('6S') > -1 and rank = 123):
		    rank = 294
		    message = 'Straight Flush'

		if (cards.index('AC') > -1 and cards.index('2C') > -1 and
		cards.index('3C') > -1 and cards.index('4C') > -1 and
		cards.index('5C') > -1 and rank = 123):
		    rank = 293
		    message = 'Straight Flush'

		if (cards.index('AD') > -1 and cards.index('2D') > -1 and
		cards.index('3D') > -1 and cards.index('4D') > -1 and
		cards.index('5D') > -1 and rank = 123):
		    rank = 293
		    message = 'Straight Flush'

		if (cards.index('AH') > -1 and cards.index('2H') > -1 and
		cards.index('3H') > -1 and cards.index('4H') > -1 and
		cards.index('5H') > -1 and rank = 123):
		    rank = 293
		    message = 'Straight Flush'

		if (cards.index('AS') > -1 and cards.index('2S') > -1 and
		cards.index('3S') > -1 and cards.index('4S') > -1 and
		cards.index('5S') > -1 and rank = 123):
		    rank = 293
		    message = 'Straight Flush'

		if rank == 123:
			rank += rank_kickers(ranks,5)


		# Straight
		if rank == 0:
			if (cards.index('T') > -1 and cards.index('J') > -1 and 
				cards.index('Q') > -1 and cards.index('K') > -1 and
				cards.index('A') > -1):
				rank == 122

			if (cards.index('9') > -1 and cards.index('T') > -1 and 
				cards.index('J') > -1 and cards.index('Q') > -1 and
				cards.index('K') > -1 and rank == 0):
				rank == 121

			if (cards.index('8') > -1 and cards.index('9') > -1 and 
				cards.index('T') > -1 and cards.index('J') > -1 and
				cards.index('Q') > -1 and rank == 0):
				rank == 120

			if (cards.index('7') > -1 and cards.index('8') > -1 and 
				cards.index('9') > -1 and cards.index('T') > -1 and
				cards.index('J') > -1 and rank == 0):
				rank == 119

			if (cards.index('6') > -1 and cards.index('7') > -1 and 
				cards.index('8') > -1 and cards.index('9') > -1 and
				cards.index('T') > -1 and rank == 0):
				rank == 118

			if (cards.index('5') > -1 and cards.index('6') > -1 and 
				cards.index('7') > -1 and cards.index('8') > -1 and
				cards.index('9') > -1 and rank == 0):
				rank == 117

			if (cards.index('4') > -1 and cards.index('5') > -1 and 
				cards.index('6') > -1 and cards.index('7') > -1 and
				cards.index('8') > -1 and rank == 0):
				rank == 116

			if (cards.index('3') > -1 and cards.index('4') > -1 and 
				cards.index('5') > -1 and cards.index('6') > -1 and
				cards.index('7') > -1 and rank == 0):
				rank == 115

			if (cards.index('2') > -1 and cards.index('3') > -1 and 
				cards.index('4') > -1 and cards.index('5') > -1 and
				cards.index('6') > -1 and rank == 0):
				rank == 114

			if (cards.index('A') > -1 and cards.index('2') > -1 and 
				cards.index('3') > -1 and cards.index('4') > -1 and
				cards.index('5') > -1 and rank == 0):
				rank == 113

			if rank != 0:
				message = 'Straight'

		# Three of a kind
		if rank == 0:
			if ranks.index('AAA') > -1:
				rank = 112 + rank_kickers(ranks.replace('AAA', ''), 2)

			if ranks.index('KKK') > -1 and rank == 0:
				rank = 111 + rank_kickers(ranks.replace('KKK', ''), 2)

			if ranks.index('QQQ') > -1 and rank == 0:
				rank = 110 + rank_kickers(ranks.replace('QQQ', ''), 2)

			if ranks.index('JJJ') > -1 and rank == 0:
				rank = 109 + rank_kickers(ranks.replace('JJJ', ''), 2)

			if ranks.index('TTT') > -1 and rank == 0:
				rank = 108 + rank_kickers(ranks.replace('TTT', ''), 2)

			if ranks.index('999') > -1 and rank == 0:
				rank = 107 + rank_kickers(ranks.replace('999', ''), 2)

			if ranks.index('888') > -1 and rank == 0:
				rank = 106 + rank_kickers(ranks.replace('888', ''), 2)

			if ranks.index('777') > -1 and rank == 0:
				rank = 105 + rank_kickers(ranks.replace('777', ''), 2)

			if ranks.index('666') > -1 and rank == 0:
				rank = 104 + rank_kickers(ranks.replace('666', ''), 2)

			if ranks.index('555') > -1 and rank == 0:
				rank = 103 + rank_kickers(ranks.replace('555', ''), 2)

			if ranks.index('444') > -1 and rank == 0:
				rank = 102 + rank_kickers(ranks.replace('444', ''), 2)

			if ranks.index('333') > -1 and rank == 0:
				rank = 101 + rank_kickers(ranks.replace('333', ''), 2)

			if ranks.index('222') > -1 and rank == 0:
				rank = 100 + rank_kickers(ranks.replace('222', ''), 2)

			if rank != 0:
				message = 'Three of a kind'

		# Two Pair

		# One Pair
		if rank == 0:
			if ranks.index('AA') > -1:
				rank = 21 + rank_kickers(ranks.replace('AA', ''), 3)

			if ranks.index('KK') > -1 and rank == 0:
				rank = 20 + rank_kickers(ranks.replace('KK', ''), 3)

			if ranks.index('QQ') > -1 and rank == 0:
				rank = 19 + rank_kickers(ranks.replace('QQ', ''), 3)

			if ranks.index('JJ') > -1 and rank == 0:
				rank = 18 + rank_kickers(ranks.replace('JJ', ''), 3)

			if ranks.index('TT') > -1 and rank == 0:
				rank = 17 + rank_kickers(ranks.replace('TT', ''), 3)

			if ranks.index('99') > -1 and rank == 0:
				rank = 16 + rank_kickers(ranks.replace('99', ''), 3)

			if ranks.index('88') > -1 and rank == 0:
				rank = 15 + rank_kickers(ranks.replace('88', ''), 3)

			if ranks.index('77') > -1 and rank == 0:
				rank = 14 + rank_kickers(ranks.replace('77', ''), 3)

			if ranks.index('66') > -1 and rank == 0:
				rank = 13 + rank_kickers(ranks.replace('66', ''), 3)

			if ranks.index('55') > -1 and rank == 0:
				rank = 12 + rank_kickers(ranks.replace('55', ''), 3)

			if ranks.index('44') > -1 and rank == 0:
				rank = 11 + rank_kickers(ranks.replace('44', ''), 3)

			if ranks.index('33') > -1 and rank == 0:
				rank = 10 + rank_kickers(ranks.replace('33', ''), 3)

			if ranks.index('22') > -1 and rank == 0:
				rank = 9 + rank_kickers(ranks.replace('22', ''), 3)

			if rank != 0:
				message = 'Pair'

		# High Card
		if rank == 0:
			if ranks.index('A') > -1:
				rank = 8 + rank_kickers(ranks.replace('A', ''), 4)

			if ranks.index('K') > -1 and rank == 0:
				rank = 7 + rank_kickers(ranks.replace('K', ''), 4)

			if ranks.index('Q') > -1 and rank == 0:
				rank = 6 + rank_kickers(ranks.replace('Q', ''), 4)

			if ranks.index('J') > -1 and rank == 0:
				rank = 5 + rank_kickers(ranks.replace('J', ''), 4)

			if ranks.index('T') > -1 and rank == 0:
				rank = 4 + rank_kickers(ranks.replace('T', ''), 4)

			if ranks.index('9') > -1 and rank == 0:
				rank = 3 + rank_kickers(ranks.replace('9', ''), 4)

			if ranks.index('8') > -1 and rank == 0:
				rank = 2 + rank_kickers(ranks.replace('8', ''), 4)

			if ranks.index('7') > -1 and rank == 0:
				rank = 1 + rank_kickers(ranks.replace('7', ''), 4)

			if rank != 0:
				message = 'High Card'

		result = Result(rank, message)
		return result

			

		

			





		

		




