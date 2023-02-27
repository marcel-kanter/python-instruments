import unittest

from instruments.oscilloscope.tektronix.tektronixmso5bhorizontal import TektronixMSO5BHorizontal
from instruments.oscilloscope import Oscilloscope


class MockOscilloscope(Oscilloscope):
	def __init__(self):
		Oscilloscope.__init__(self)


class TektronixMSO5BHorizontalTestCase(unittest.TestCase):
	def test_creation(self):
		oscilloscope = MockOscilloscope()

		TektronixMSO5BHorizontal(oscilloscope)
