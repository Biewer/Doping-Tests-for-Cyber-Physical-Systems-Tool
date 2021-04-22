from ValueSet import *

class EmptySet(ValueSet):
	"""Represents the empty set"""
	def __init__(self):
		super(EmptySet, self).__init__()

	def get_any_value(self):
		raise Exception('No value available!')

	def get_random_value(self):
		raise Exception('No value available!')

	def is_empty(self):
		return True
