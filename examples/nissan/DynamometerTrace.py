import os, sys
sys.path.insert(0, os.path.abspath("../"))

from tool.doping_monitor import RecordedTrace
from tool.doping_test import Input, Output

class DynamometerTrace(RecordedTrace):
	"""A recorded trace on dynamometer and PEMS"""
	def __init__(self, file_name):
		super(DynamometerTrace, self).__init__(file_name)

	# Each line is either an input or an output.
	# The first letter in each line is either "i" (for input) or "o" (for output)
	# followed by the string representation of a float
	def get_symbol_from_string(self, strng):
		if strng[0] == 'i':
			# this is an input
			# parse the value
			number = float(strng[1:])

			return Input(number)
		elif strng[0] == 'o':
			# we have an output
			# parse the value
			number = float(strng[1:])

			return Output(number)
		else:
			raise Exception('Unknown file format! (' + strng + ')')





if __name__ == '__main__':
	m = DynamometerTrace('examples/nissan/NEDC.txt')
	print(m)

