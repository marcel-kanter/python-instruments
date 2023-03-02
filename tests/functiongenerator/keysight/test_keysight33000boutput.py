import unittest

from instruments.functiongenerator.keysight.keysight33000boutput import Keysight33000BOutput
from instruments.functiongenerator import FunctionGenerator


class MockFunctionGenerator(FunctionGenerator):
	def __init__(self):
		FunctionGenerator.__init__(self)


class Keysight33000BOutputTestCase(unittest.TestCase):
	def test_creation(self):
		generator = MockFunctionGenerator()

		with self.assertRaises(ValueError):
			Keysight33000BOutput(generator, 0)

		Keysight33000BOutput(generator, 1)
