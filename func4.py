#Nested Function
def fun1():
	def fun2():
		return "Inner Function"
		
	print("Outer Function")
	print(fun2())
fun1()

def fun3(a):
	def fun4(b):
		return a+b
	return fun4
a=fun3(3)(4)
print(a)

def a(q,w):
	def b(e):
		return q+w * e
	return b
num=a(2,3)(4) 
print(num)

#Recursion
def a1(num):
	if num==1:
		return 1
	else:
		return num * a1(num-1)
print("Factorial using recursion.....\nThe answer is:",a1(5))

def tailSum(num,accumulator=0):
	if num==0:
		return accumulator
	else:
		return tailSum(num-1, accumulator+num )
print("TAIL SUM:",tailSum(10))

#lambda
v1=lambda x: x * 2
print(v1(5))

v2=lambda x,y:x+y
print(v2(5,1000))


v3=lambda x,y:('Greater is Y:',y) if x<y else ('Greater is X:',x)
print(v3(1,3))

v4=lambda x,y:x if x>y else y
print(v4(8,3))
