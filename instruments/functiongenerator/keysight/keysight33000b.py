from ..functiongenerator import FunctionGenerator
from .keysight33000boutput import Keysight33000BOutput
from .keysight33000bsource import Keysight33000BSource
from .keysight33000btrigger import Keysight33000BTrigger


class Keysight33000B(FunctionGenerator):
	def __init__(self, channel_count):
		if int(channel_count) <= 0:
			raise ValueError("channel_count must be an integer greater than 0")

		FunctionGenerator.__init__(self)
		self._resource = None

		self.source = {}
		self.output = {}
		self.trigger = {}
		for slot in range(1, 1 + channel_count):
			self.source[slot] = Keysight33000BSource(self, slot)
			self.output[slot] = Keysight33000BOutput(self, slot)
			self.trigger[slot] = Keysight33000BTrigger(self, slot)

	def close(self):
		if self._resource is not None:
			self._resource.close()
			self._resource = None

	def identity(self):
		ident = self._resource.query("*IDN?")
		return ident

	def open(self, name, resource_manager):
		self._resource = resource_manager.open_resource(name)
		self._resource.write_termination = "\n"
		self._resource.read_termination = "\n"

	def query(self, s):
		return self._resource.query(s)

	def read(self):
		return self._resource.read()

	def reset(self):
		self._resource.write("*CLS;*RST")
		self._resource.query("*OPC?")

	def write(self, s):
		self._resource.write(s)
