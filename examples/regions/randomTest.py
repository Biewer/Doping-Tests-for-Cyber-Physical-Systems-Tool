import os, sys
sys.path.insert(0, os.path.abspath("../"))

from DynamometerTrace import *
from LastComponentDistance import *
from ECU import *
from RandomInputSelection import *
from tool.doping_monitor import MonitoredStandard
from tool.doping_test import AcceptanceChecker, DT




def main():
	# kappa_i = 15 km/h
	input_threshold = 15
	# past-forgetful distance function d(i1, i2) = |i1 - i2|
	input_distance = LastComponentDistance(input_threshold, Input)

	# kappa_o = 180 mg/km
	output_threshold = 180
	# past-forgetful distance function d(o1, o2) = |o1 - o2|
	output_distance = LastComponentDistance(output_threshold, Output)

	# a perfect NEDC drive is simulated in nedc_standard.txt
	# DynamometerTrace uses RecordedTrace from the monitoring part of the tool,
	# however, we use that only to load the NEDC standard trace
	nedc = DynamometerTrace('./examples/regions/nedc_standard.txt')

	# create the standard using the only standard 'NEDC'
	standard = MonitoredStandard([nedc])

	# SUT (System Under Test)
	# In contrast to monitoring, we use 
	system_under_test = ECU()

	# limit tests to the length of the NEDC (1180s) plus 1 output
	boundary = 1181

	# resolve non-determinism by randomness
	test_case_selection = RandomInputSelection(input_distance, standard, boundary)

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