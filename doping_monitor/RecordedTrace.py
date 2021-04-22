import os, sys
sys.path.insert(0, os.path.abspath("../"))

from tool.doping_test import SimpleTrace

from MonitorUnderTest import *
from MonitorTestCaseSelection import *

class RecordedTrace(SimpleTrace):
	"""Abstract class that represents a recorded trace and can generate a test case selection and system under test, that can rerun the recorded trace."""
	def __init__(self, file_name):
		super(RecordedTrace, self).__init__()
		self.file_name = file_name
		self._load_trace()
		self.symbolPosition = 0

		self._SUT = None
		self._TCSelection = None


	def _load_trace(self):
		with open(self.file_name) as f:
			for line in f:
				# convert the line to a symbol
				symbol = self.get_symbol_from_string(line)
				self.extend(symbol)

	
	def get_symbol_from_string(self, str):
		# How to parse a trace is left to be specified for concrete input and output domains
		raise NotImplementedError('Abstract method not implemented!')

	# returns the symbol at the current symbol position
	def get_current_symbol(self):
		if self.symbolPosition < len(self):
			return self[self.symbolPosition]
		else:
			return None

	# moves the symbol position to the next symbol
	def advance_symbol(self):
		self.symbolPosition += 1

	# this method checks if the input passed by DT matches the input forwarded by MonitorTestCaseSelection
	def assert_input(self, inp):
		if self.symbolPosition == 0 or self[self.symbolPosition-1] != inp:
			raise Exception('Input provided by monitor does not match input forwarded by DT!')



	# the following methods create a SUT and test case selection; they both work together such that the trace is replayed by DT
	def get_system_under_test(self):
		if self._SUT == None:
			self._SUT = MonitorUnderTest(self)

		return self._SUT


	def get_test_case_selection(self):
		if self._TCSelection == None:
			self._TCSelection = MonitorTestCaseSelection(self)

		return self._TCSelection



