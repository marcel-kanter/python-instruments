from .tektronixhorizontal import TektronixHorizontal


class TektronixMSO5BHorizontal(TektronixHorizontal):
	"""
	Class for the horizontal subsystem of the Tektronix MSO5B series oscilloscopes.
	"""

	def __init__(self, parent):
		TektronixHorizontal.__init__(self, parent)
