class Logger(object):
	devMode = True;
	
	@staticmethod
	def debug(msg):
		if Logger.devMode:
			print(msg) 
	
	@staticmethod		
	def info(msg):
		print(msg) 
	
		