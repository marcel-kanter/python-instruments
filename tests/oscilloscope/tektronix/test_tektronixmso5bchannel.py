import unittest

from instruments.oscilloscope.tektronix.tektronixmso5bchannel import TektronixMSO5BChannel
from instruments.oscilloscope import Oscilloscope


class MockOscilloscope(Oscilloscope):
	def __init__(self):
		Oscilloscope.__init__(self)


class TektronixMSO5BChannelChannelTestCase(unittest.TestCase):
	def test_creation(self):
		oscilloscope = MockOscilloscope()

		with self.assertRaises(ValueError):
			TektronixMSO5BChannel(oscilloscope, 0)

		TektronixMSO5BChannel(oscilloscope, 1)
