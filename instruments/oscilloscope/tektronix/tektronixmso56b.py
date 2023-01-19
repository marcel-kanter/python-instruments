from .tektronixmso5b import TektronixMSO5B


class TektronixMSO56B(TektronixMSO5B):
	def __init__(self):
		TektronixMSO5B.__init__(self, 6)
