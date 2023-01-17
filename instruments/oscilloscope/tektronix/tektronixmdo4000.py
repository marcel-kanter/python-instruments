from ..oscilloscope import Oscilloscope


class TektronixMDO4000(Oscilloscope):
	def __init__(self):
		Oscilloscope.__init__(self)
		self._resource = None

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

	def reset(self):
		self._resource.write("*CLS;*RST")
		self._resource.query("*OPC?")
