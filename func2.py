def func2(lis):
	print("Passing values:",lis)
	lis[2]=100
	print("Changed Values:",lis)
lis1=[1,2,3,4]
func2(lis1)
print("Outside Value:",lis1)

def func3(*a):
	for b in a:
		print("Value:",b)
func3(1,2,3,4,5,6)
