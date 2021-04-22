import os, sys
sys.path.insert(0, os.path.abspath("../"))


from LastComponentDistance import *
from NoisyStandard import *
from NoisyMirror import *

from ManualTestCaseSelection import *



def main():
	# limit tests to 20 inputs/outputs (i.e. use DT_20)
	boundary = 20

	# use the manual test case selection (see class ManualTestCaseSelection)
	test_case_selection = ManualTestCaseSelection(boundary)

	tests_to_execute = test_case_selection.get_available_tests()

	# allow user to specify a subset of the tests
	if len(sys.argv) > 1:
		tests_to_execute = sys.argv[1:]
	else:
		print('Hint: You can also execute only a subset of the tests by passing the test names as additional arguments.')

	# iterate over all available tests
	for test_instance in tests_to_execute:
		print('----------\nSelecting ' + test_instance)

		# we reinitialize all instances in case some component is memory-aware (e.g. DT is)
	
		# kappa_i = 0.2
		input_threshold = 0.2
		# past-forgetful distance function d(i1, i2) = |i1 - i2|
		input_distance = LastComponentDistance(input_threshold, Input)

		# kappa_o = 0.5
		output_threshold = 0.5
		# past-forgetful distance function d(o1, o2) = |o1 - o2|
		output_distance = LastComponentDistance(output_threshold, Output)

		# Std (subset of SUT)
		standard = NoisyStandard()

		# SUT (System Under Test)
		system_under_test = NoisyMirror()

		# use the default output verifier
		output_verifier = AcceptanceChecker(boundary, input_distance, output_distance, standard)

		# DT_boundary
		tester = DT(test_case_selection, output_verifier, system_under_test)
		
		test_case_selection.set_active_test(test_instance)

		# run the test
		test_result = tester.test(boundary)

		# give user feedback
		print('Test Trace:\n' + str(test_result.history) + '\n')
		if test_result.passed():
			print("Test passed!")
		else:
			print("Test FAILED for Standard Trace:")
			print(test_result.standard_trace)



if __name__ == '__main__':
	main()



	