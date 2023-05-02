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

	@property
	def frequency(self):
		return self.parent.query(f"SOUR{self.slot}:FREQ?")

	@frequency.setter
	def frequency(self, f):
		self.parent.write(f"SOUR{self.slot}:FREQ {f}")

	@property
	def phase(self):
		return self.parent.query(f"SOUR{self.slot}:PHAS?")

	@phase.setter
	def phase(self, v):
		self.parent.write(f"SOUR{self.slot}:PHAS {v}")

	@property
	def voltage(self):
		return self.parent.query(f"SOUR{self.slot}:VOLT?")

	@voltage.setter
	def voltage(self, v):
		self.parent.write(f"SOUR{self.slot}:VOLT {v}")

	@property
	def voltage_high(self):
		return self.parent.query(f"SOUR{self.slot}:VOLT:HIGH?")

	@voltage_high.setter
	def voltage_high(self, v):
		self.parent.write(f"SOUR{self.slot}:VOLT:HIGH {v}")

	@property
	def voltage_low(self):
		return self.parent.query(f"SOUR{self.slot}:VOLT:LOW?")

	@voltage_low.setter
	def voltage_low(self, v):
		self.parent.write(f"SOUR{self.slot}:VOLT:LOW {v}")

	@property
	def voltage_offset(self):
		return self.parent.query(f"SOUR{self.slot}:OFFS?")

	@voltage_offset.setter
	def voltage_offset(self, v):
		self.parent.write(f"SOUR{self.slot}:VOLT:OFFS {v}")

	@property
	def voltage_unit(self):
		return self.parent.query(f"SOUR{self.slot}:VOLT:UNIT?")

	@voltage_unit.setter
	def voltage_unit(self, v):
		self.parent.write(f"SOUR{self.slot}:VOLT:UNIT {v}")
