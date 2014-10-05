'''
This module contains an example run of a poker game using the poker engine
'''

from table import Table

poker_table = Table(50,100,2,10,100,1000)

poker_table.add_player('bob',1000)
poker_table.add_player('jane',1000)
poker_table.add_player('dylan',1000)
poker_table.add_player('john',1000)

poker_table.start_game()
#print poker_table.game.round_name
poker_table.players[1].call()
poker_table.players[2].call()
poker_table.players[3].call()
poker_table.players[0].call()

#print poker_table.game
#print poker_table.game.round_name
poker_table.players[1].call()
poker_table.players[2].call()
poker_table.players[3].call()
poker_table.players[0].call()
#print poker_table.game.round_name
poker_table.players[1].call() #bet(50)
poker_table.players[2].call()
#poker_table.players[1].call()
#poker_table.players[2].call()
poker_table.players[3].call()
poker_table.players[0].call()
#print poker_table.game.round_name
poker_table.players[1].call()
poker_table.players[2].call()
poker_table.players[3].call()
poker_table.players[0].call()
#print poker_table.game.round_name
# poker_table.players[1].call()
# poker_table.players[2].call()
# poker_table.players[3].call()
# poker_table.players[0].call()

print poker_table.game