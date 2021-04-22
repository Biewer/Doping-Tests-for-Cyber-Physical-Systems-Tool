from TraceIterator import *
# import ExtendedTrace

class Trace(object):
	"""Abstract class for representing a trace"""
	def __init__(self):
		super(Trace, self).__init__()

	def __iter__(self):
		return TraceIterator(self)

	def extend(self, symbol):
		# Add a symbol at the end of the trace
		raise NotImplementedError()

	def __len__(self):
		raise NotImplementedError()

	def __getitem__(self, key):
		raise NotImplementedError()
		