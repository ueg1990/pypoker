
from table import Table
from player import Player
from deck import Deck
from game import Game

def main():
	table = Table(50,100,2,10,100,1000)
	player = Player('usman', 1000, table)
	deck = Deck()
	game = Game(50,100)
	# print table
	#print sorted(deck.deck)
	# print player
	#print Game(50,100)
	
if __name__ == "__main__":
    main()