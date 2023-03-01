from .tektronixtrigger import TektronixTrigger


class TektronixMDO4000Trigger(TektronixTrigger):
	def __init__(self, parent):
		TektronixTrigger.__init__(self, parent)
