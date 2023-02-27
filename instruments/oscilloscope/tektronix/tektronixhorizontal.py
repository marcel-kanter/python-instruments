class TektronixHorizontal(object):
	def __init__(self, parent):
		self.parent = parent

	@property
	def delay_mode(self):
		return self.parent.query(f"HOR:DEL:MOD?")

	@delay_mode.setter
	def delay_mode(self, v):
		self.parent.write(f"HOR:DEL:MOD {v}")

	@property
	def delay_time(self):
		v = self.parent.query(f"HOR:DEL:TIM?")
		return float(v)

	@delay_time.setter
	def delay_time(self, v):
		self.parent.write(f"HOR:DEL:TIM {v}")

	@property
	def position(self):
		v = self.parent.query(f"HOR:POS?")
		return float(v)

	@position.setter
	def position(self, v):
		self.parent.write(f"HOR:POS {v}")

	@property
	def recordlength(self):
		v = self.parent.query(f"HOR:RECO?")
		return int(v)

	@recordlength.setter
	def recordlength(self, v):
		self.parent.write(f"HOR:RECO {v}")

	@property
	def samplerate(self):
		v = self.parent.query(f"HOR:SAMPLER?")
		return int(v)

	@samplerate.setter
	def samplerate(self, v):
		self.parent.write(f"HOR:SAMPLER {v}")

	@property
	def scale(self):
		v = self.parent.query(f"HOR:SCAL?")
		return float(v)

	@scale.setter
	def scale(self, v):
		self.parent.write(f"HOR:SCAL {v}")
