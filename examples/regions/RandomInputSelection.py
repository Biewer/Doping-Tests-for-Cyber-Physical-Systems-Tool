from tool.doping_test import TestCaseSelection, RandomTestCaseSelection, Input
#from Input import *
import random

class RandomInputSelection(RandomTestCaseSelection):
	"""This class extends `RandomTestCaseSelection`, however it does not pick Omega_case randomly, but uses the knowledge, that we need 1180 inputs followed by one output."""
	def __init__(self, input_distance, standard, boundary):
		super(RandomInputSelection, self).__init__(input_distance, standard, boundary)
	

	def get_next_option(self, history):
		if len(history) == 1180:
			# We know that DT must check the output
			return TestCaseSelection.OPTION_OUTPUT
		elif len(history) == 1181:
			# The test length is 1180s, after that, pass
			return TestCaseSelection.OPTION_PASS
		else:
			# the first 1180 seconds are used to pass speed inputs to the car
			return TestCaseSelection.OPTION_INPUT




