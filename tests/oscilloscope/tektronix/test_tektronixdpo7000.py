import unittest


from instruments.oscilloscope.tektronix.tektronixdpo7000 import TektronixDPO7000


class TektronixDPO7000TestCase(unittest.TestCase):
	def test_instance(self):
		with self.assertRaises(ValueError):
			TektronixDPO7000(0)

		examinee = TektronixDPO7000(1)
		channel1 = examinee.channel[1]

		with self.assertRaises(KeyError):
			examinee.channel[2]
