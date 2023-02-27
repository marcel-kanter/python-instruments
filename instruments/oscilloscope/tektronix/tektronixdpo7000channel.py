from .tektronixchannel import TektronixChannel


class TektronixDPO7000Channel(TektronixChannel):
	def __init__(self, parent, slot):
		TektronixChannel.__init__(self, parent, slot)
