import os, sys
sys.path.insert(0, os.path.abspath("../"))
from tool.doping_test import *

class ECU(SystemUnderTest):
	"""This class implements an engine control unit, that simulates software doping based on the findings in VW ECUs"""
	def __init__(self):
		super(ECU, self).__init__()
		# remember history to determine if a trip leaves the region
		self.history = SimpleTrace() 
		# load the piecewise linear functions (sampled in steps of 1s) that define a region
		self.nedc_lower = self.load_function('./examples/regions/nedc_lower.txt')
		self.nedc_upper = self.load_function('./examples/regions/nedc_upper.txt')
		self.logging_enabled = False


	def load_function(self, filename):
		file = open(filename, 'r')
		data = file.read()
		# Lists contain string representations of floats seperated by whitespace
		items = data.split()
		float_items = map(float, items)
		return float_items
		

	def log(self, msg):
		if self.logging_enabled:
			print(msg)


	def pass_input(self, inp):
		if not isinstance(inp, Input):
			raise Exception('Expected input!')

		inp = inp.value 	# unwrap input

		# Check if output is available. This is only the case after 1180s.
		o = self.receive_output()
		if o != None:
			# If output is available, pass it to DT
			return o

		# Otherwise add the input to the history
		self.history.extend(inp)
		return None



	def receive_output(self):
		# We do not implement a timeout here, because we do not wait for a concurrent system
		if len(self.history) == 1180:
			# NEDC is over, compute some output
			assert(len(self.nedc_lower) == len(self.nedc_upper) == 1180)
			# The variable `region_was_left` is set to True, once the current trip leaves the region
			region_was_left = False
			# We compute the total distance of the current trip iteratively
			total_distance = 0.0
			for i in xrange(0, 1180):
				# inputs are in km/h, so we have to convert the value to m/s
				total_distance += self.history[i]/3.6
				# we check if the current trip left the region after time i (but we are only interested in the first time this happens)
				if not region_was_left and (total_distance < self.nedc_lower[i] or total_distance > self.nedc_upper[i]):
					# Output some debug information
					self.log("Region violation after %d seconds:\n  Current trip distance: %f.\n  NEDC lower threshold: %f.\n  NEDC upper threshold: %f." % (i, total_distance, self.nedc_lower[i], self.nedc_upper[i]))
					region_was_left = True
			# The total length of the NEDC as defined is pre-computed
			total_nedc_distance = 11036
			# compute the ratio of the current trip length and NEDC length
			distance_ratio = 1.0 - (total_distance / total_nedc_distance)
			# We want the NOx to correlate to some extend to the kilometers driven
			nox_ratio = distance_ratio * (3.0/4.0)
			result = Output(50.0 * (1 + nox_ratio))
			if region_was_left:
				# if the region was left, we increase the amount of NOx by 7.3
				result = Output(7.3 * result.value)
			# we remember that we produced the output
			self.history.extend(result)
			return result
		
		return None





# Debugging only
def main():
	prog = ECU()

	# enable logging for testing
	prog.logging_enabled = True

	print(prog.nedc_lower)


if __name__ == '__main__':
	main()
