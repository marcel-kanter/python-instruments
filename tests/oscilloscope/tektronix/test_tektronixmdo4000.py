import unittest


from instruments.oscilloscope.tektronix.tektronixmdo4000 import TektronixMDO4000


class TektronixMDO4000TestCase(unittest.TestCase):
	def test_instance(self):
		with self.assertRaises(ValueError):
			TektronixMDO4000(0)

		examinee = TektronixMDO4000(1)
		channel1 = examinee.channel[1]

		with self.assertRaises(KeyError):
			examinee.channel[2]
