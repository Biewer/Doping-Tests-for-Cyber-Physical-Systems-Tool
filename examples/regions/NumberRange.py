from tool.doping_test.ValueSet import *
import random

class NumberRange(ValueSet):
	"""Contains all numbers >= min and <= max"""
	def __init__(self, min, max):
		super(NumberRange, self).__init__()
		self.min = min
		self.max = max

	def get_any_value(self):
		if self.is_empty():
			raise Exception('No value available!')
		else:
			return self.min

	def get_random_value(self):
		if self.is_empty():
			raise Exception('No value available!')
		else:
			return random.uniform(self.min, self.max)

	def is_empty(self):
		return self.max < self.min

	def __str__(self):
		return '[' + str(self.min) + ',' + str(self.max) + ']'

	def __repr__(self):
		return str(self)
		