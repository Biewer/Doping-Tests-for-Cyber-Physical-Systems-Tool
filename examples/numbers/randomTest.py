import os, sys
sys.path.insert(0, os.path.abspath("../"))


from LastComponentDistance import *
from NoisyStandard import *
from NoisyMirror import *



def main():
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

	# limit tests to 20 inputs/outputs
	boundary = 20

	# resolve non-determinism by randomness
	test_case_selection = RandomTestCaseSelection(input_distance, standard, boundary)

	# use the default output verifier
	output_verifier = AcceptanceChecker(boundary, input_distance, output_distance, standard)

	# DT_boundary
	tester = DT(test_case_selection, output_verifier, system_under_test)

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