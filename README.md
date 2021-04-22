# Readme

This code is an evaluated artifact complementing the TOMACS publication "Doping Tests for Cyber-Physical Systems".

## This folder contains the following artifacts:

- Our testing and monitoring framework, as described in the appendix of our paper
- The NEDC inputs with a single invented output in the last line:
  examples/regions/nedc_standard.txt
- The pair of piecewise linear functions found in a Volkswagen ECU, sampled with an interval of 1s:
  examples/regions/nedc_lower.txt and examples/regions/nedc_upper.txt
- The recorded traces of our tests with the Nissan car:
  examples/nissan/NEDC.txt, examples/nissan/PowerNEDC.txt and examples/nissan/SineNEDC.txt
- Examples for using our tool, partially using the artifacts listed above


## Requirements

All examples were tested on Mac OS 10.15.3 and Python 2.7.16.
Python installers can be downloaded here: https://www.python.org/downloads/release/python-2716/.


## Execution

All examples must be executed from the root folder of the tool. The following examples can be run:

- `python examples/numbers/randomTest.py`
- `python examples/numbers/predefinedTest.py`
- `python examples/numbers/monitoring.py`
- `python examples/regions/randomTest.py`
- `python examples/nissan/checkPowerNEDC.py`
- `python examples/nissan/checkSineNEDC.py`