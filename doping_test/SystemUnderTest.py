class SystemUnderTest(object):
	"""This is an interface to a concrete implementation under test"""
	def __init__(self):
		super(SystemUnderTest, self).__init__()
	
	# pass_input either forwards an input to the system under test, or if there is some output from the SUT that
	# has not yet been forwarded to DT, it ignores the input and delivers the new output by returning it to the caller
	def pass_input(self, inp):
		raise NotImplementedError('Abstract method not implemented!')


	# this method forwards an output from the SUT to the caller. If no output is available, it blocks until an output is
	# available, or (after some timeout) returns None to indicate quiescence
	def receive_output(self):
		raise NotImplementedError('Abstract method not implemented!')