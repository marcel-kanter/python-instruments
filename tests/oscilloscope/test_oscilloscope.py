import unittest


from instruments.oscilloscope import Oscilloscope


class OscilloscopeTestCase(unittest.TestCase):
	def test_instance(self):
		examinee = Oscilloscope()

		with self.assertRaises(NotImplementedError):
			examinee.open()

		with self.assertRaises(NotImplementedError):
			examinee.identity()

		with self.assertRaises(NotImplementedError):
			examinee.reset()

		with self.assertRaises(NotImplementedError):
			examinee.close()
