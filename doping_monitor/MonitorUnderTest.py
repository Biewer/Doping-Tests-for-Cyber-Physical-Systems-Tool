import os, sys
sys.path.insert(0, os.path.abspath("../"))

from tool.doping_test import SystemUnderTest, Output

class MonitorUnderTest(SystemUnderTest):
	"""This class provides exactly the values provided by recordedTrace"""
	def __init__(self, recordedTrace):
		super(MonitorUnderTest, self).__init__()
		self.recordedTrace = recordedTrace


	def pass_input(self, inp):
		# reassure that the correct input was passed
		self.recordedTrace.assert_input(inp)


	def receive_output(self):
		# get the output from the recordedTrace
		next_symbol = self.recordedTrace.get_current_symbol()

		# reassure that it is an output
		if isinstance(next_symbol, Output):
			# advance the internal symbol position of the recordedTrace to the next symbol
			self.recordedTrace.advance_symbol()
			return next_symbol
		else:
			# if the symbol is not an output, warn the user and return quiescence
			print('Warning! DT requested an output although no output is available.')
			return Output(None)
