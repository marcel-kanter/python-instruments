import unittest


from instruments.oscilloscope.tektronix import TektronixMSO56B


class TektronixDPO7104TestCase(unittest.TestCase):
	def test_instance(self):
		examinee = TektronixMSO56B()
