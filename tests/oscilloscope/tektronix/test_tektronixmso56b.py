import unittest


from instruments.oscilloscope.tektronix import TektronixMSO56B


class TektronixDPO7104TestCase(unittest.TestCase):
	def test_instance(self):
		examinee = TektronixMSO56B()
		channel1 = examinee.channel[1]
		channel2 = examinee.channel[2]
		channel3 = examinee.channel[3]
		channel4 = examinee.channel[4]
		channel5 = examinee.channel[5]
		channel6 = examinee.channel[6]
