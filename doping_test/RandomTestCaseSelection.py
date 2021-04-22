from TestCaseSelection import *
from Input import *
import random

class RandomTestCaseSelection(TestCaseSelection):
	"""Test case selection that randomly selects a case and inputs."""
	def __init__(self, input_distance, standard, boundary):
		super(RandomTestCaseSelection, self).__init__()
		self.input_distance = input_distance
		self.standard = standard
		self.boundary = boundary

		# We pick any standard trace as reference for new inputs
		self.standard_trace = self.standard.get_any_trace(self.boundary)
	

	def get_next_option(self, history):
		r = random.randint(0,99)
		# 10% for pass
		if r < 10:
			return TestCaseSelection.OPTION_PASS
		# 45% for input
		if r < 55:
			return TestCaseSelection.OPTION_INPUT
		# 45% for output
		return TestCaseSelection.OPTION_OUTPUT

	
	def get_next_input(self, history):
		# refine the range to values that have a distance of at most kappa_i to the standard trace we picked
		close_values = self.input_distance.get_input_symbols_close_to_trace(self.standard_trace, history)

		if close_values.is_empty():
			# if there are no close values, get the set of all inputs
			input_domain = self.input_distance.get_values_domain()

			# return any of them
			return Input(input_domain.get_random_value())
		else:
			# pick any of the close values
			return Input(close_values.get_random_value())

