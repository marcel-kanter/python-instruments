import unittest


from instruments.functiongenerator.keysight import Keysight33522B


class Keysight33522BTestCase(unittest.TestCase):
	def test_instance(self):
		examinee = Keysight33522B()
		channel1 = examinee.channel[1]
		channel2 = examinee.channel[2]
