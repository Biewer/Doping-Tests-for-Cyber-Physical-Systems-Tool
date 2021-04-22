import os, sys
sys.path.insert(0, os.path.abspath("../"))

from RecordedNumberTrace import *
from LastComponentDistance import *
from tool.doping_monitor import MonitoredStandard
from tool.doping_test import AcceptanceChecker, DT



def main():
	all_runs = ['./examples/numbers/run-fail.txt', './examples/numbers/run-pass.txt']

	for run in all_runs:
		print('----------\nChecking ' + run)


		# check the recorded data in the run file
		monitor = RecordedNumberTrace(run)

		# the traces are recorded in std1.txt and std2.txt
		std1 = RecordedNumberTrace('./examples/numbers/run-std1.txt')
		std2 = RecordedNumberTrace('./examples/numbers/run-std2.txt')

		# create the standard using the two monitor instances std1 and std2
		standard = MonitoredStandard([std1, std2])

		# SUT (System Under Test) is provided by the monitor in order to support monitoring
		system_under_test = monitor.get_system_under_test()

		# similarly, use the test case selection particularly designed for monitoring
		test_case_selection = monitor.get_test_case_selection()

		# test are bounded to 20 symbols (i.e. we want to use DT_20)
		boundary = 20


		# kappa_i = 0.2
		input_threshold = 0.2
		# past-forgetful distance function d(i1, i2) = |i1 - i2|
		input_distance = LastComponentDistance(input_threshold, Input)

		# kappa_o = 0.5
		output_threshold = 0.5
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
