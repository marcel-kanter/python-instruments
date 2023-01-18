import unittest


from instruments.powersupply.rohdeschwarz import RohdeSchwarzHMP4040


class RohdeSchwarzHMP4040TestCase(unittest.TestCase):
	def test_instance(self):
		examinee = RohdeSchwarzHMP4040()
