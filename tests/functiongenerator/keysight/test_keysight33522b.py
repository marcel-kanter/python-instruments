import unittest


from instruments.functiongenerator.keysight import Keysight33522B


class Keysight33522BTestCase(unittest.TestCase):
	def test_instance(self):
		examinee = Keysight33522B()
		output1 = examinee.output[1]
		output2 = examinee.output[2]
