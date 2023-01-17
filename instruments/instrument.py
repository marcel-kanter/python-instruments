class Instrument(object):
	def __init__(self):
		pass

	def close(self):
		raise NotImplementedError()

	def identity(self):
		raise NotImplementedError()

	def open(self, *args):
		raise NotImplementedError()

	def reset(self):
		raise NotImplementedError()
