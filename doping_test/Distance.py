class Distance(object):
	"""Abstract class that defines the interface that the implementations of distance functions must adhere to."""
	def __init__(self, values_domain, threshold):
		super(Distance, self).__init__()
		self.values_domain = values_domain
		self.threshold = threshold

	def get_values_domain(self):
		return self.values_domain


	# returns 'True' iff for all j <= len(trace): trace_1[j] == trace_2[j]
	def are_traces_equal(self, trace_1, trace_2):
		raise NotImplementedError('Abstract method not implemented!')


	# This method can be used to optimise test input selection. It returns a set (e.g. ValueSet) of all possible inputs i, 
	# such that trace and history.extend(i) are still close enough to be considered by robust cleanness
	def get_input_symbols_close_to_trace(self, trace, history):
		raise NotImplementedError('Abstract method not implemented!')

	# Returns all traces sigma in `standard` that satisfy V(boundary, sigma, history)
	def get_relevant_standard_traces(self, standard, history, boundary):
		raise NotImplementedError('Abstract method not implemented!')

	# Find an output in one of the traces in standard_traces, that satiesfies the second condition of the 
	# definition of robust cleanness for \sigma = trace and \sigma' = history.
	# `input_distance` may be used to check whether two traces have the same input projection.
	def find_close_output_for_standard_trace(self, trace, standard_traces, history, input_distance):
		raise NotImplementedError('Abstract method not implemented!')
		