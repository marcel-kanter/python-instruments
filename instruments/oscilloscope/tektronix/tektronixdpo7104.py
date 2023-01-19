from .tektronixdpo7000 import TektronixDPO7000


class TektronixDPO7104(TektronixDPO7000):
	def __init__(self):
		TektronixDPO7000.__init__(self, 4)
