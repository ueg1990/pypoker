'''
This module defines a class to store the rank of a given hand
'''

class Result(object):

	def __init__(self, rank, message):
		self.rank = rank
		self.message = message

	def __str__(self):
		return self.rank + " " + self.message