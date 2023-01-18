import unittest


from instruments.datalogger.keysight import KeysightDAQ970A


class KeysightDAQ970ATestCase(unittest.TestCase):
	def test_instance(self):
		examinee = KeysightDAQ970A()
