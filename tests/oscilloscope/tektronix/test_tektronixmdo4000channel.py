import unittest

from instruments.oscilloscope.tektronix.tektronixmdo4000channel import TektronixMDO4000Channel
from instruments.oscilloscope import Oscilloscope


class MockOscilloscope(Oscilloscope):
	def __init__(self):
		Oscilloscope.__init__(self)


class TektronixMDO4000ChannelTestCase(unittest.TestCase):
	def test_creation(self):
		oscilloscope = MockOscilloscope()

		with self.assertRaises(ValueError):
			TektronixMDO4000Channel(oscilloscope, 0)

		TektronixMDO4000Channel(oscilloscope, 1)
