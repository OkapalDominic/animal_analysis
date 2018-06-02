from abc import ABCMeta, abstractmethod

class IModel:
	__metaclass__ = ABCMeta

	"""
		Returns the labels detected
		@params: photo is the image to look at
	"""
	def labelImage(self,photo):
		pass