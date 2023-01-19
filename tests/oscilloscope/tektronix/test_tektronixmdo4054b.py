import unittest


from instruments.oscilloscope.tektronix import TektronixMDO4054B


class TektronixDPO7104TestCase(unittest.TestCase):
	def test_instance(self):
		examinee = TektronixMDO4054B()
		channel1 = examinee.channel[1]
		channel2 = examinee.channel[2]
		channel3 = examinee.channel[3]
		channel4 = examinee.channel[4]
