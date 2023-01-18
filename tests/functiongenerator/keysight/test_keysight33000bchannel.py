import unittest

from instruments.functiongenerator.keysight.keysight33000bchannel import Keysight33000BChannel
from instruments.functiongenerator import FunctionGenerator


class MockFunctionGenerator(FunctionGenerator):
	def __init__(self):
		FunctionGenerator.__init__(self)


class Keysight33000BChannelTestCase(unittest.TestCase):
	def test_creation(self):
		generator = MockFunctionGenerator()

		with self.assertRaises(ValueError):
			Keysight33000BChannel(generator, 0)

		Keysight33000BChannel(generator, 1)
