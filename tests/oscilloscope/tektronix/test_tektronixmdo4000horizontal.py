import unittest

from instruments.oscilloscope.tektronix.tektronixmdo4000horizontal import TektronixMDO4000Horizontal
from instruments.oscilloscope import Oscilloscope


class MockOscilloscope(Oscilloscope):
	def __init__(self):
		Oscilloscope.__init__(self)


class TektronixMDO4000HorizontalTestCase(unittest.TestCase):
	def test_creation(self):
		oscilloscope = MockOscilloscope()

		TektronixMDO4000Horizontal(oscilloscope)
