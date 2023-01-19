import unittest


from instruments.oscilloscope.tektronix import TektronixDPO7104


class TektronixDPO7104TestCase(unittest.TestCase):
	def test_instance(self):
		examinee = TektronixDPO7104()
		channel1 = examinee.channel[1]
		channel2 = examinee.channel[2]
		channel3 = examinee.channel[3]
		channel4 = examinee.channel[4]
