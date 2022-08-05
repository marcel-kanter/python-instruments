import unittest


from instruments import Instrument


class InstrumentTestCase(unittest.TestCase):
	def test_instance(self):
		examinee = Instrument()

		with self.assertRaises(NotImplementedError):
			examinee.identity()
