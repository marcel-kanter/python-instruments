import unittest


from instruments.oscilloscope.tektronix import TektronixMDO4054B


class TektronixDPO7104TestCase(unittest.TestCase):
	def test_instance(self):
		examinee = TektronixMDO4054B()
