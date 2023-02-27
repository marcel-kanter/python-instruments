from .tektronixhorizontal import TektronixHorizontal


class TektronixDPO7000Horizontal(TektronixHorizontal):
	"""
	Class for the horizontal subsystem of the DPO7000 series oscilloscopes.
	"""

	def __init__(self, parent):
		TektronixHorizontal.__init__(self, parent)

	@property
	def recordlength(self):
		v = self.parent.query(f"HOR:MODE:RECO?")
		return int(v)

	@recordlength.setter
	def recordlength(self, v):
		self.parent.write(f"HOR:MODE:RECO {v}")

	@property
	def samplerate(self):
		v = self.parent.query(f"HOR:MODE:SAMPLER?")
		return int(v)

	@samplerate.setter
	def samplerate(self, v):
		v = self.parent.query(f"HOR:MODE:SAMPLER {v}")

	@property
	def scale(self):
		v = self.parent.query(f"HOR:MODE:SCAL?")
		return float(v)

	@scale.setter
	def scale(self, v):
		self.parent.write(f"HOR:MODE:SCAL {v}")
