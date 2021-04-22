class Output(object):
	"""This class represents outputs. Mainly, this class used to be able to distinguish between inputs and outputs."""
	def __init__(self, value):
		super(Output, self).__init__()
		self.value = value


	def __str__(self):
		return 'out(' + str(self.value) + ')'

	def __repr__(self):
		return str(self)
		