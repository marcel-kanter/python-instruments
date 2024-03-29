import unittest

from instruments.functiongenerator.keysight.keysight33000boutput import Keysight33000BOutput
from instruments.functiongenerator import FunctionGenerator


class MockFunctionGenerator(FunctionGenerator):
	def __init__(self):
		FunctionGenerator.__init__(self)

		self.read_data = None
		self.write_data = None

	def read(self):
		return self.read_data

	def query(self, s):
		self.write(s)
		return self.read()

	def write(self, s):
		self.write_data = s


class Keysight33000BSourceTestCase(unittest.TestCase):
	def test_creation(self):
		generator = MockFunctionGenerator()

		with self.assertRaises(ValueError):
			Keysight33000BOutput(generator, 0)

		Keysight33000BOutput(generator, 1)

	def test_load(self):
		generator = MockFunctionGenerator()
		channel = 2
		examinee = Keysight33000BOutput(generator, channel)

		for load in (0, 10001):
			with self.subTest("load=" + str(load)):
				with self.assertRaises(ValueError):
					examinee.load = load

		for load in (1, 50, 100, float("inf")):
			with self.subTest("load=" + str(load)):
				generator.write_data = None
				examinee.load = load
				self.assertEqual(generator.write_data, "OUTP" + str(channel) + ":LOAD " + str(load))
