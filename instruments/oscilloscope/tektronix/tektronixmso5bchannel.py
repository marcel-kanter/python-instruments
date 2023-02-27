from .tektronixchannel import TektronixChannel


class TektronixMSO5BChannel(TektronixChannel):
	def __init__(self, parent, slot):
		TektronixChannel.__init__(self, parent, slot)
