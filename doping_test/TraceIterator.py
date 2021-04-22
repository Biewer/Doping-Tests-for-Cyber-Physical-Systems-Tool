class TraceIterator(object):
	"""Class for iterating traces"""
	def __init__(self, trace):
		super(TraceIterator, self).__init__()
		# The trace to iterate on
		self.trace = trace

		self._traceLength = len(trace)
		# The index of the next symbol to be returned
		self._nextIndex = 0

	def next(self):
		# Check if we reached the end of the trace
		if self._nextIndex >= self._traceLength:
			raise StopIteration()

		# If not, return a symbol and increase the internal counter
		res = self.trace[self._nextIndex]
		self._nextIndex = self._nextIndex + 1

		return res
		