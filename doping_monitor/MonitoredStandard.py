import os, sys
sys.path.insert(0, os.path.abspath("../"))

from tool.doping_test import Standard

class MonitoredStandard(Standard):
	"""This standard consists of all traces given by assigned recorded traces."""
	def __init__(self, recorded_traces):
		super(MonitoredStandard, self).__init__()
		self.recorded_traces = recorded_traces

		# we need at least one trace, i.e. one monitor, for 'get_any_trace'
		if len(self.recorded_traces) == 0:
			raise Exception('MonitoredStandard needs at least one monitor!')

	def get_any_trace(self, boundary):
		# return the full trace of the first monitor
		return self.recorded_traces[0]

	def get_traces(self, boundary):
		return self.recorded_traces
