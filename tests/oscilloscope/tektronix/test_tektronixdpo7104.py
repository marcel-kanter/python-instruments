import unittest


from instruments.oscilloscope.tektronix import TektronixDPO7104


class TektronixDPO7104TestCase(unittest.TestCase):
	def test_instance(self):
		examinee = TektronixDPO7104()
