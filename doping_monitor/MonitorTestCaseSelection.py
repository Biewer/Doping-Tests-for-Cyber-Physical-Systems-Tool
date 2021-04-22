import os, sys
sys.path.insert(0, os.path.abspath("../"))

from tool.doping_test import TestCaseSelection, Input

class MonitorTestCaseSelection(TestCaseSelection):
	"""test case selection that instructs DT according to the data of recordedTrace"""
	def __init__(self, recordedTrace):
		super(MonitorTestCaseSelection, self).__init__()
		self.recordedTrace = recordedTrace

	def get_next_option(self, history):
		# check the current symbol of the recordedTrace
		next_symbol = self.recordedTrace.get_current_symbol()

		#if it is None, we are at the end of the stream and terminate the testing
		if next_symbol == None:
			return TestCaseSelection.OPTION_PASS
		# if it is an input, we chosse option 2 of DT
		if isinstance(next_symbol, Input):
			return TestCaseSelection.OPTION_INPUT
		# if the next symbol is an output, we pick option 3 of DT
		else:
			return TestCaseSelection.OPTION_OUTPUT

	def get_next_input(self, history):
		# get the input from the recordedTrace
		next_symbol = self.recordedTrace.get_current_symbol()

		# reassure that it is an input
		if isinstance(next_symbol, Input):
			# advance the internal symbol position of the recordedTrace to the next symbol
			self.recordedTrace.advance_symbol()
			return next_symbol
		else:
			# complain otherwise
			raise Exception('No input available!')