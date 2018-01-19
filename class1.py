class a1:
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def mul(self):
		val=self.x*self.y
		self.test="VMVMVM"
		print(val)
a,b=input("Enter the Number1 and 2:").split()
a=int(a)
b=int(b)
obj1=a1(a,b)
obj1.mul()
print(getattr(obj1,'test'))
