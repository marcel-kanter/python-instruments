class TektronixTrigger(object):
	def __init__(self, parent):
		self.parent = parent

	@property
	def state(self):
		return self.parent.query(f"TRIG:STATE?")
