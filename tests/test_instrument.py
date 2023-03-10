import unittest


from instruments import Instrument


class InstrumentTestCase(unittest.TestCase):
	def test_instance(self):
		examinee = Instrument()

		with self.assertRaises(NotImplementedError):
			examinee.open()

		with self.assertRaises(NotImplementedError):
			examinee.identity()

		with self.assertRaises(NotImplementedError):
			examinee.reset()

		with self.assertRaises(NotImplementedError):
			examinee.read()

		with self.assertRaises(NotImplementedError):
			examinee.query("")

		with self.assertRaises(NotImplementedError):
			examinee.write("")

		with self.assertRaises(NotImplementedError):
			examinee.close()
