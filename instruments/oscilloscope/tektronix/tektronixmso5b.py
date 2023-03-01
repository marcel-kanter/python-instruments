from ..oscilloscope import Oscilloscope
from .tektronixmso5bchannel import TektronixMSO5BChannel
from .tektronixmso5bhorizontal import TektronixMSO5BHorizontal
from .tektronixmso5btrigger import TektronixMSO5BTrigger


class TektronixMSO5B(Oscilloscope):
	def __init__(self, channel_count):
		if int(channel_count) <= 0:
			raise ValueError("channel_count must be an integer greater than 0")

		Oscilloscope.__init__(self)
		self._resource = None

		self.channel = {}
		for slot in range(1, 1 + channel_count):
			self.channel[slot] = TektronixMSO5BChannel(self, slot)

		self.horizontal = TektronixMSO5BHorizontal(self)
		self.trigger = TektronixMSO5BTrigger(self)

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
