class Keysight33000BSource(object):
	_functions = ("SIN", "SINUSOID", "SQUARE", "SQU", "TRIANGLE", "TRI", "RAMP", "PULSE", "PRBS", "NOISE", "NOIS", "ARB", "DC")

	def __init__(self, parent, slot):
		if int(slot) <= 0:
			raise ValueError("slot must be an integer greater than 0")

		self.parent = parent
		self.slot = int(slot)

	@property
	def function(self):
		return self.parent.query(f"SOUR{self.slot}:FUNC?")

	@function.setter
	def function(self, f):
		if f not in self._functions:
			raise ValueError("f must be one of " + str(self._functions))

		self.parent.write(f"SOUR{self.slot}:FUNC {f}")
