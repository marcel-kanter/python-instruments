import unittest

from instruments.oscilloscope.tektronix.tektronixdpo7000channel import TektronixDPO7000Channel
from instruments.oscilloscope import Oscilloscope


class MockOscilloscope(Oscilloscope):
	def __init__(self):
		Oscilloscope.__init__(self)


class TektronixDPO7000ChannelTestCase(unittest.TestCase):
	def test_creation(self):
		oscilloscope = MockOscilloscope()

		with self.assertRaises(ValueError):
			TektronixDPO7000Channel(oscilloscope, 0)

		TektronixDPO7000Channel(oscilloscope, 1)
