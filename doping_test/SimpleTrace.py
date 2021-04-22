import Trace

class SimpleTrace(Trace.Trace):
	"""Implements the simples form of traces, which is represented by a list of inputs and outputs"""
	def __init__(self, value_list=None, boundary=0):
		super(SimpleTrace, self).__init__()
		# Can be initialised with a list of inputs and outputs
		if value_list == None:
			value_list = []
		self.value_list = value_list
		self.boundary = boundary	# this field is to mark a trace as bounded without having to copy the whole prefix

	def extend(self, symbol):
		self.value_list.append(symbol)


	def __len__(self):
		if self.boundary > 0:
			return min(len(self.value_list), self.boundary)
		else:
			return len(self.value_list)

	def __getitem__(self, key):
		if self.boundary > 0 and key >= self.boundary:
			raise KeyError('Index out of (artificial) bounds!')

		return self.value_list[key]

	def __str__(self):
		# Returns a human readable string representation of the trace
		c = 0
		res = ''
		for val in self.value_list:
			if c > 0:
				res += ' --> '

			c += 1
			res += str(val)

			if self.boundary > 0 and c >= self.boundary:
				res += ' --> ...'
				break

		return res