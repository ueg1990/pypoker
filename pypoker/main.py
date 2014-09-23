
from table import Table
from player import Player
from deck import Deck

def main():
	table = Table(50,100,2,10,100,1000)
	player = Player('usman', 1000, table)
	deck = Deck()
	print table
	print deck
	print player
	
if __name__ == "__main__":
    main()