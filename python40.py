class shape(object):
	def __init__(self):
		pass	
	def area(self):
		return 0
class square(shape):
	def __init__(self,l):
		#shape.__init__(self)		
		self.length=l
	def area(self):
		return self.length**2
obj=square(95)
print(obj.area())
