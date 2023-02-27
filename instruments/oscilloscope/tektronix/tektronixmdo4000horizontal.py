from .tektronixhorizontal import TektronixHorizontal


class TektronixMDO4000Horizontal(TektronixHorizontal):
	"""
	Class for the horizontal subsystem of the MDO4000 series oscilloscopes.
	"""

	def __init__(self, parent):
		TektronixHorizontal.__init__(self, parent)
