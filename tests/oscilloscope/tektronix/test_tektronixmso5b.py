import unittest


from instruments.oscilloscope.tektronix.tektronixmso5b import TektronixMSO5B


class TektronixMSO5BTestCase(unittest.TestCase):
	def test_instance(self):
		with self.assertRaises(ValueError):
			TektronixMSO5B(0)

		examinee = TektronixMSO5B(1)
		channel1 = examinee.channel[1]

		with self.assertRaises(KeyError):
			examinee.channel[2]
