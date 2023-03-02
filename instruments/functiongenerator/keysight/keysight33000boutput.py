class Keysight33000BOutput(object):
	def __init__(self, parent, slot):
		if int(slot) <= 0:
			raise ValueError("slot must be an integer greater than 0")

		self.parent = parent
		self.slot = int(slot)

	@property
	def load(self):
		l = self.parent.query(f"OUTPUT{self.slot}:LOAD?")
		if l == "9.9E+37":
			return float("INF")
		else:
			return float(l)

	@load.setter
	def load(self, l):
		if l != float("INF") and (l < 1 or l > 10000):
			raise ValueError("l must be infinity or between 1 and 10000")

		self.parent.write(f"OUTP{self.slot}:LOAD {l}")
