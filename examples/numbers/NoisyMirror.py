import os, sys
sys.path.insert(0, os.path.abspath("../"))
from tool.doping_test import *


# from SystemUnderTest import *
# from Input import *
# from Output import *
import random
import math

from NoisyStandard import *

class NoisyMirror(SystemUnderTest):
	"""This class implements a noisy identity function"""
	def __init__(self):
		super(NoisyMirror, self).__init__()
		self.next_output = None 	# None means 'no output available'
		self.logging_enabled = False
		self.do_doping = True


	def decimals_after_point(self, x):
		s = str(x)
		if not '.' in s:
			return 0
		return len(s) - s.index('.') - 1

	def log(self, msg):
		if self.logging_enabled:
			print(msg)


	def pass_input(self, inp):
		if not isinstance(inp, Input):
			raise Exception('Expected input!')

		inp = inp.value 	# unwrap input

		# check if output is available
		if self.next_output != None:
			o = self.next_output
			self.next_output = None
			return o

		# process input and store output in next_output
		if not self.do_doping or self.decimals_after_point(inp) < 3:	
			k = random.randint(1, 2)
			self.log('factor is ' + str(k))
			self.next_output = Output(float(inp)*k)
		# software doping happens here: some clever engineer thought, 
		# that test arguments never have more than two decimals, so 
		# the system returns potentially larger values when there are 
		# more than 2 decimals in the input
		else:
			k = random.randint(1, 4)
			self.log('factor is ' + str(k))
			self.next_output = Output(float(inp)*k)

		return None



	def receive_output(self):
		# We do not implement a timeout here, because we do not wait on a concurrent system
		o = self.next_output
		self.next_output = None
		return o






def main():
	prog = NoisyMirror()

	# enable logging for testing
	prog.logging_enabled = True

	while True:
		# read user input
		inp = raw_input('Enter a number (or enter "std" to print all standard traces): ')

		# check if std was requested
		if inp == 'std':
			standard = NoisyStandard()
			boundary_string = raw_input('Select a boundary for traces: ')
			boundary = int(boundary_string)

			standard_traces = standard.get_traces(boundary)
			i = 1

			for trace in standard_traces:
				print('Standard Trace #' + str(i) + ':')
				i = i + 1
				print(trace)
				print('')

			return

		# parse it as a float and wrap into an Input
		number = Input(float(inp))

		# pass the input the program; there should not be a waiting output
		outp = prog.pass_input(number)
		if outp != None:
			raise Exception('Did not except this output :/')

		# receive the next output; there must always be one
		outp = prog.receive_output()
		if outp == None:
			raise Exception('Expected output was not delivered :/')

		# print the output to the console
		print('-> ' + str(outp.value))


if __name__ == '__main__':
	main()
