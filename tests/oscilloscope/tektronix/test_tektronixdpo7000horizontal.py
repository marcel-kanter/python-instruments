import unittest

from instruments.oscilloscope.tektronix.tektronixdpo7000horizontal import TektronixDPO7000Horizontal
from instruments.oscilloscope import Oscilloscope


class MockOscilloscope(Oscilloscope):
	def __init__(self):
		Oscilloscope.__init__(self)


class TektronixDPO7000HorizontalTestCase(unittest.TestCase):
	def test_creation(self):
		oscilloscope = MockOscilloscope()

		TektronixDPO7000Horizontal(oscilloscope)
