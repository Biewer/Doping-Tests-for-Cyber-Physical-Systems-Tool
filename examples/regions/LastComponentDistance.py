from tool.doping_test.Distance import *
from NumberRange import *
from tool.doping_test.EmptySet import *
from tool.doping_test.Input import *
from tool.doping_test.Output import *

class LastComponentDistance(Distance):
	"""The distance is the absolute difference of the last number in each trace"""
	def __init__(self, threshold, measuredValueType):
		numbers = NumberRange(0.0, float(10E6-1))
		super(LastComponentDistance, self).__init__(numbers, threshold)
		self.measuredValueType = measuredValueType

		# make sure that values have either type 'Input' or 'Output'
		if (measuredValueType != Input and measuredValueType != Output):
			raise Exception('Unsupported value type!')

	def get_input_symbols_close_to_trace(self, trace, history):
		k = len(history)
		if len(trace) <= k:
			print(len(trace), k)
			raise Exception('incompatible history!')

		trace_value = trace[k]

		if isinstance(trace_value, Input):
			res = NumberRange(max(0.0, trace_value.value - self.threshold), trace_value.value + self.threshold)
			return res
		elif isinstance(trace_value, Output):
			# the distance from an output to any input is infinite
			return EmptySet()
		else:
			raise Exception('Was expecting either input or output!')

	def get_distance_of_symbols(self, symbol_1, symbol_2):
		if not isinstance(symbol_1, self.measuredValueType):
			if isinstance(symbol_2, self.measuredValueType):
				return float('inf')
			else:
				return 0
		if not isinstance(symbol_2, self.measuredValueType):
			# we know that symbol_1 is self.measuredValueType
			return float('inf')

		if symbol_1.value == None or symbol_2.value == None:
			# one of the symbols is quiescence
			if symbol_1.value == None and symbol_2.value == None:
				return 0
			else:
				return float('inf')


		return abs(symbol_1.value - symbol_2.value)

	def are_traces_equal(self, trace_1, trace_2):
		if len(trace_1) != len(trace_2):
			return False

		for j in xrange(0, len(trace_1)):
			if self.get_distance_of_symbols(trace_1[j], trace_2[j]) > 10E-9:
				return False

		return True


	def get_relevant_standard_traces(self, standard, history, boundary):
		all_traces = standard.get_traces(boundary)

		# initially, the set of relevant traces is empty
		res = []

		# iterate all standard traces and check them
		for standard_trace in all_traces:
			j = 0
			# iterate over single symbols as long as the condition is valid
			while j < len(history) and self.get_distance_of_symbols(standard_trace[j], history[j]) <= self.threshold+10E-9:
				j = j + 1

			if j >= len(history):
				# if the reason for loop termination was that j exceeded the limit, the trace is relevant
				res.append(standard_trace)

		return res 





	def find_close_output_for_standard_trace(self, trace, standard_traces, history, input_distance):
		# First, check if 'trace' matches the condition
		o_history = history[len(history)-1]
		o_trace = trace[len(history)-1]

		if self.get_distance_of_symbols(o_history, o_trace) <= self.threshold:
			# o_trace is close enough to satisfy the condition
			return o_trace

		for std_trace in standard_traces:
			if std_trace == trace:
				# don't check this trace a second time
				continue

			# check if inputs(std_trace) == inputs(trace)
			if input_distance.are_traces_equal(trace, std_trace):

				o_std_trace = std_trace[len(history) - 1]
				if self.get_distance_of_symbols(o_history, o_std_trace) <= self.threshold:
					# o_std_trace is close enough to satisfy the condition
					return o_std_trace

		return None





