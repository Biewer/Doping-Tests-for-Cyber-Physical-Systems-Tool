class ValueSet(object):
	"""Abstract class for representation of value sets"""
	def __init__(self):
		super(ValueSet, self).__init__()
	
	def get_any_value(self):
		# Return any of the values in the set. Two calls may return different values.
		raise NotImplementedError('Abstract method not implemented!')

	def get_random_value(self):
		# Randomly sample a value from the set. Each value must have a probability >0 to be selected.
		raise NotImplementedError('Abstract method not implemented!')

	def is_empty(self):
		# Returns True if no values are in the set.
		raise NotImplementedError('Abstract method not implemented!')