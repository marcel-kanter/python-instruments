from .tektronixchannel import TektronixChannel


class TektronixMDO4000Channel(TektronixChannel):
	def __init__(self, parent, slot):
		TektronixChannel.__init__(self, parent, slot)
