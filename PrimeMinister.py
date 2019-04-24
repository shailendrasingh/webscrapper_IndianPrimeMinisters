from Logger import Logger

class PrimeMinister(object):
	
	def __init__(self):
		# initialization
		self._name = ''
		self._date = ''
		
		
	def setName(self, n):
		self._name = n
		
	def getName(self):
		return self._name
		
	def setDate(self, d):
		self._date = d
	
	def getDate(self):
		return self._date
	
	name = property(getName, setName) 
	date = property(getDate, setDate) 
	