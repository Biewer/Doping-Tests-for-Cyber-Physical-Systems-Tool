from tool.doping_test import TestCaseSelection, Input, Output
import math

class ManualTestCaseSelection(TestCaseSelection):
	"""Test are predefined by a human"""
	def __init__(self, boundary):
		super(ManualTestCaseSelection, self).__init__()
		self.boundary = boundary

		self.active_test = self.test1
		self.test_instruction = self.next_test_instruction
		self.next_step = 0


	def set_active_test(self, test_name):
		self.next_step = 0

		if test_name == 'good-test1':
			self.active_test = self.test1
			self.test_instruction = self.next_test_instruction
		elif test_name == 'good-test2':
			self.active_test = self.test2
			self.test_instruction = self.next_test_instruction
		elif test_name == 'bad-test1':
			self.active_test = self.test3
			self.test_instruction = self.next_test_instruction
		elif test_name == 'bad-test2':
			self.active_test = self.test4
			self.test_instruction = self.wrong_test_instruction
		else:
			raise Exception('Test not found!')

	def get_available_tests(self):
		return ['good-test1', 'good-test2', 'bad-test1', 'bad-test2']


	# test1 asks for inputs s-0.1, where s is a standard input
	def test1(self, s):
		return s - 0.1

	# like test1, but the distance to s decreases monotonically
	def test2(self, s):
		distance_to_s = 1.0/(10*s)
		return s - distance_to_s

	# this is a test that does not satisfy the input property and hence allows any output
	def test3(self, s):
		# the input distance will be > kappa_i at s = 3
		# also starting from s = 3, there are more than 3 decimals, so doping is not detected
		return s - (0.1 * math.sqrt(4*(s-1)))	

	# test 4 does the mistake, that it waits for an output when it should give an input
	# this causes the input distance to go to infinity and hence > kappa_i
	def test4(self, s):
		distance_to_s = 1.0/(5*s)
		return s + distance_to_s




	def next_test_instruction(self):
		if self.next_step % 2 == 0:
			# provide a new input (step/2+1)-th input (starting with 1)
			return Input(self.active_test(int(self.next_step/2)+1))
		else:
			return Output(None)	# here, this means that an output should be expected

	def wrong_test_instruction(self):
		if self.next_step == 2:
			return Output(None)
		else:
			return self.next_test_instruction()



	def get_next_option(self, history):
		if self.next_step > self.boundary:
			# let the test pass when we have enough steps (option one of DT)
			return TestCaseSelection.OPTION_PASS

		# check what the function wants to do next
		instruction = self.test_instruction()



		# if it wants to provide an input, choose the second option of DT, otherwise option three
		if isinstance(instruction, Input):
			# defer step counter increase until after input was provided
			return TestCaseSelection.OPTION_INPUT
		else:
			# increase step counter
			self.next_step += 1
			return TestCaseSelection.OPTION_OUTPUT

	def get_next_input(self, history):
		# check what the function wants to do next
		instruction = self.test_instruction()

		# make sure that we actually want to provide an input
		self.next_step += 1
		if isinstance(instruction, Input):
			return instruction
		else:
			raise Exception('No input available!')

