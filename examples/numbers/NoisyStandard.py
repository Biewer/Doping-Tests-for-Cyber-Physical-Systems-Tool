from tool.doping_test.Standard import *
from tool.doping_test.Input import *
from tool.doping_test.Output import *
from tool.doping_test.SimpleTrace import *


class NoisyStandard(Standard):
	"""Represents the standard behaviour of NoisyMirror"""
	def __init__(self):
		super(NoisyStandard, self).__init__()

		self.values_k_1 = None
		self.values_k_2 = None 


	def get_any_trace(self, boundary):
		return self.get_traces(boundary)[0]

	def get_traces(self, boundary):
		# check if values are already computed
		if self.values_k_1 == None or self.values_k_2 == None or len(self.values_k_1) != boundary or len(self.values_k_2) != boundary:

			# inputs are all natural numbers
			inputs = xrange(1, boundary+1)

			# create the empty trace for k=1 and k=2 in the computation algorithm
			self.values_k_1 = SimpleTrace([], boundary)	# Note that we do not use the boundary functionality of the trace here, because we generate the trace of the aprropriate size directly
			self.values_k_2 = SimpleTrace([], boundary)

			number_of_items = 0

			for inp in inputs:
				# add the current input
				self.values_k_1.extend(Input(float(inp)))
				self.values_k_2.extend(Input(float(inp)))
				
				number_of_items = number_of_items + 1
				if number_of_items >= boundary:
					# We added enough values (note that the for-loop without the breaks would produce 2*boundary values)
					break


				# add the corresponding output
				self.values_k_1.extend(Output(float(inp)*1))		# o = i * 1
				self.values_k_2.extend(Output(float(inp)*2))		# o = i * 2

				number_of_items = number_of_items + 1
				if number_of_items >= boundary:
					break

		return [self.values_k_2, self.values_k_1]


