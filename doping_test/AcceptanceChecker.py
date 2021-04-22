from Output import *

class AcceptanceChecker(object):
	"""This is an implementation of acc_b from the paper."""

	QUIESCENCE = Output(None)

	def __init__(self, boundary, input_distance, output_distance, standard):
		super(AcceptanceChecker, self).__init__()
		self.boundary = boundary
		self.input_distance = input_distance
		self.output_distance = output_distance
		self.standard = standard

		self.printed_trivial_passing_warning = False
	
	def check_output(self, history):

		# get the standard traces that are close (w.r.t. inputs) to the full history
		close_standard_traces = self.input_distance.get_relevant_standard_traces(self.standard, history, self.boundary)

		if len(close_standard_traces) == 0 and not self.printed_trivial_passing_warning:
			# If inputs deviate too much, the test passes independently of the output.
			# This is not desired, hence print a warning
			print('Warning: input deviates by more than kappa_i! (' + str(history) + ')')
			self.printed_trivial_passing_warning = True

		for standard_trace in close_standard_traces:
			# This line of code tries to find an output that satiesfies the second condition of the definition of robust cleanness
			satisfying_output = self.output_distance.find_close_output_for_standard_trace(standard_trace, close_standard_traces, history, self.input_distance)
			
			if satisfying_output == None:
				# When we do not find such an output for standard_trace, return the trace (it can be used as a counter example)
				return standard_trace

		# We found a satisfying output for every standard trace, i.e. return None to indicate that no standard trace violates the property
		return None


	def check_quiescence(self, history):
		# This method exists to allow special handling of quiescence in subclasses; here, we only forward the call to `check_output`
		return self.check_output(history)

