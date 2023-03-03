class TektronixChannel(object):
	def __init__(self, parent, slot):
		if int(slot) <= 0:
			raise ValueError("slot must be an integer greater than 0")

		self.parent = parent
		self.slot = int(slot)

	@property
	def coupling(self):
		return self.parent.query(f"CH{self.slot}:COUP?")

	@coupling.setter
	def coupling(self, v):
		self.parent.write(f"CH{self.slot}:COUP {v}")


	@property
	def offset(self):
		v = self.parent.query(f"CH{self.slot}:OFFS?")
		return float(v)

	@offset.setter
	def offset(self, v):
		self.parent.write(f"CH{self.slot}:OFFS {v}")

	@property
	def position(self):
		v = self.parent.query(f"CH{self.slot}:POS?")
		return float(v)

	@position.setter
	def position(self, v):
		self.parent.write(f"CH{self.slot}:POS {v}")

	@property
	def scale(self):
		v = self.parent.query(f"CH{self.slot}:SCAL?")
		return float(v)

	@scale.setter
	def scale(self, v):
		self.parent.write(f"CH{self.slot}:SCAL {v}")

	@property
	def skew(self):
		v = self.parent.query(f"CH{self.slot}:DESK?")
		return float(v)

	@skew.setter
	def skew(self, v):
		self.parent.write(f"CH{self.slot}:DESK {v}")

	@property
	def state(self):
		return self.parent.query(f"SEL:CH{self.slot}?")

	@state.setter
	def state(self, v):
		self.parent.write(f"SEL:CH{self.slot} {v}") 

	@property
	def termination(self):
		v = self.parent.query(f"CH{self.slot}:TER?")
		return float(v)

	@termination.setter
	def termination(self, v):
		self.parent.write(f"CH{self.slot}:TER {v}")
