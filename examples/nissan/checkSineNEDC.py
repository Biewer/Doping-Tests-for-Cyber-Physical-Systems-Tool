import os, sys
sys.path.insert(0, os.path.abspath("../"))

from DynamometerTrace import *
from LastComponentDistance import *
from tool.doping_monitor import MonitoredStandard
from tool.doping_test import AcceptanceChecker, DT



def main():
	# check the recorded data in the run file
	monitor = DynamometerTrace('./examples/nissan/SineNEDC.txt')

	# the NEDC drive is recorded in NEDC.txt
	nedc = DynamometerTrace('./examples/nissan/NEDC.txt')

	# create the standard using the only standard 'NEDC'
	standard = MonitoredStandard([nedc])

	# SUT (System Under Test) is provided by the monitor in order to support monitoring
	system_under_test = monitor.get_system_under_test()

	# similarly, use the test case selection particularly designed for monitoring
	test_case_selection = monitor.get_test_case_selection()

	# the length of an NEDC is 1180s; we have 1180 inputs and one output at the end
	boundary = 1181


	# kappa_i = 15km/h
	input_threshold = 15
	# past-forgetful distance function d(i1, i2) = |i1 - i2|
	input_distance = LastComponentDistance(input_threshold, Input)

	# kappa_o = 180mg/km
	output_threshold = 180
	# past-forgetful distance function d(o1, o2) = |o1 - o2|
	output_distance = LastComponentDistance(output_threshold, Output)

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
