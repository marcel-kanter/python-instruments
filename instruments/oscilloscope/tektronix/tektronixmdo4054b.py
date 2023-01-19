from .tektronixmdo4000 import TektronixMDO4000


class TektronixMDO4054B(TektronixMDO4000):
	def __init__(self):
		TektronixMDO4000.__init__(self, 4)
