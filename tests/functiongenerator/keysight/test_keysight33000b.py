import unittest


from instruments.functiongenerator.keysight.keysight33000b import Keysight33000B


class Keysight33000BTestCase(unittest.TestCase):
	def test_instance(self):
		with self.assertRaises(ValueError):
			Keysight33000B(0)

		examinee = Keysight33000B(1)
		output1 = examinee.output[1]

		with self.assertRaises(KeyError):
			examinee.output[2]
