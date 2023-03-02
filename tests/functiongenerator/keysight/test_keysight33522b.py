import unittest


from instruments.functiongenerator.keysight import Keysight33522B


class Keysight33522BTestCase(unittest.TestCase):
	def test_instance(self):
		examinee = Keysight33522B()
		source1 = examinee.source[1]
		output1 = examinee.output[1]
		trigger1 = examinee.trigger[1]
		source2 = examinee.source[2]
		output2 = examinee.output[2]
		trigger2 = examinee.trigger[2]
