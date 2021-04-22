class Input(object):
	"""This class represents inputs. Mainly, this class used to be able to distinguish between inputs and outputs."""
	def __init__(self, value):
		super(Input, self).__init__()
		self.value = value
		

	def __str__(self):
		return 'in(' + str(self.value) + ')'

	def __repr__(self):
		return str(self)