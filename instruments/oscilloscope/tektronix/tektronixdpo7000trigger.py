from .tektronixtrigger import TektronixTrigger


class TektronixDPO7000Trigger(TektronixTrigger):
	def __init__(self, parent):
		TektronixTrigger.__init__(self, parent)
