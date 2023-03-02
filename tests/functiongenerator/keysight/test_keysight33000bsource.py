import unittest

from instruments.functiongenerator.keysight.keysight33000bsource import Keysight33000BSource
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
			Keysight33000BSource(generator, 0)

		Keysight33000BSource(generator, 1)

	def test_function(self):
		generator = MockFunctionGenerator()
		channel = 2
		examinee = Keysight33000BSource(generator, channel)

		with self.assertRaises(ValueError):
			examinee.function = "X"

		for f in ("SIN", "SINUSOID", "SQUARE", "SQU", "TRIANGLE", "TRI", "RAMP", "PULSE", "PRBS", "NOISE", "NOIS", "ARB", "DC"):
			with self.subTest("f=" + str(f)):
				generator.write_data = None
				examinee.function = f
				self.assertEqual(generator.write_data, "SOUR" + str(channel) + ":FUNC " + f)
