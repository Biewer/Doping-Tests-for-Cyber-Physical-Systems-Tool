from tool.doping_monitor import RecordedTrace
from tool.doping_test import Input, Output

class RecordedNumberTrace(RecordedTrace):
	"""A recorded sequences of floats"""
	def __init__(self, file_name):
		super(RecordedNumberTrace, self).__init__(file_name)

	# Each line is either an input or an output.
	# The first letter in each line is either "i" (for input) or "o" (for output)
	# followed by the string representation of a float
	def get_symbol_from_string(self, str):
		if str[0] == 'i':
			# this is an input
			# parse the value
			number = float(str[1:])

			return Input(number)
		elif str[0] == 'o':
			# we have an output
			# parse the value
			number = float(str[1:])

			return Output(number)
		else:
			raise Exception('Unknown file format!')






