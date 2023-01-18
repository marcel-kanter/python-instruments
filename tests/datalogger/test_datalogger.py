import unittest


from instruments.datalogger import DataLogger


class DataLoggerTestCase(unittest.TestCase):
	def test_instance(self):
		examinee = DataLogger()

		with self.assertRaises(NotImplementedError):
			examinee.open()

		with self.assertRaises(NotImplementedError):
			examinee.identity()

		with self.assertRaises(NotImplementedError):
			examinee.reset()

		with self.assertRaises(NotImplementedError):
			examinee.close()
