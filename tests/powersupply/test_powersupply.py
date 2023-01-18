import unittest


from instruments.powersupply import PowerSupply


class PowerSupplyTestCase(unittest.TestCase):
	def test_instance(self):
		examinee = PowerSupply()

		with self.assertRaises(NotImplementedError):
			examinee.open()

		with self.assertRaises(NotImplementedError):
			examinee.identity()

		with self.assertRaises(NotImplementedError):
			examinee.reset()

		with self.assertRaises(NotImplementedError):
			examinee.close()
