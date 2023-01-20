class Instrument(object):
	"""
	The base class for all instruments.
	"""
	def __init__(self):
		pass

	def close(self):
		"""
		Close the connection to the instrument.
		"""
		raise NotImplementedError()

	def identity(self):
		"""
		Return the identity string for the instrument.
		"""
		raise NotImplementedError()

	def open(self, *args):
		"""
		Open a connection to the instrument.
		"""
		raise NotImplementedError()

	def read(self):
		"""
		Read data from the instrument.
		"""
		raise NotImplementedError()

	def reset(self):
		"""
		Reset the instrument to a known state.
		"""
		raise NotImplementedError()

	def query(self, s):
		"""
		Write data to the instrument and then read data from it.
		"""
		raise NotImplementedError()

	def write(self, s):
		"""
		Write data to the instrument
		"""
		raise NotImplementedError()
