class Standard(object):
	"""Abstract class for representation of Standard LTS"""
	def __init__(self):
		super(Standard, self).__init__()
	
	def get_any_trace(self, boundary):
		# Return any of the traces of standard LTS S
		raise NotImplementedError('Abstract method not implemented!')

	def get_traces(self, boundary):
		# Return all traces up to length `boundary`
		raise NotImplementedError('Abstract method not implemented!')

