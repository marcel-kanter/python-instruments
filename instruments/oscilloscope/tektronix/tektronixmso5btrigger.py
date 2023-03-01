from .tektronixtrigger import TektronixTrigger


class TektronixMSO5BTrigger(TektronixTrigger):
	def __init__(self, parent):
		TektronixTrigger.__init__(self, parent)
