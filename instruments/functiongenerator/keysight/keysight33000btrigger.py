class Keysight33000BTrigger(object):
	def __init__(self, parent, slot):
		if int(slot) <= 0:
			raise ValueError("slot must be an integer greater than 0")

		self.parent = parent
		self.slot = int(slot)
