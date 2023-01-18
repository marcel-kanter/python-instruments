import unittest


from instruments.functiongenerator import FunctionGenerator


class FunctionGeneratorTestCase(unittest.TestCase):
	def test_instance(self):
		examinee = FunctionGenerator()

		with self.assertRaises(NotImplementedError):
			examinee.open()

		with self.assertRaises(NotImplementedError):
			examinee.identity()

		with self.assertRaises(NotImplementedError):
			examinee.reset()

		with self.assertRaises(NotImplementedError):
			examinee.close()
