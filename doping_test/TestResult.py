class TestResult(object):
	"""Class for representing the result of a test (passed/failed) and additional information."""

	PASSED = True
	FAILED = False

	def __init__(self, passed, history, std_trace=None):
		super(TestResult, self).__init__()
		# Is the test passed or failed?
		self.__passed = passed

		# For which history is the test conclusive (which is the history given to DT when it decided the test outcome)?
		self.history = history

		# If the test fails, which is the standard trace for which the system under test failed?
		self.standard_trace = std_trace

	def passed(self):
		return self.__passed

	def failed(self):
		return not self.__passed

	
