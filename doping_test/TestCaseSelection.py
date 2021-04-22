class TestCaseSelection(object):
	"""This class representents concrete implementations for test case selection startegies."""

	# Three options for the three cases (as in Algorithm 1 from the paper)
	OPTION_PASS = 1
	OPTION_INPUT = 2
	OPTION_OUTPUT = 3


	def __init__(self):
		super(TestCaseSelection, self).__init__()
		

	def get_next_option(self, history):
		# Omega_case
		raise NotImplementedError('Abstract method not implemented!')

	def get_next_input(self, history):
		# Omega_In
		raise NotImplementedError('Abstract method not implemented!')