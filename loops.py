import random
a=random.randrange(0,100,5)
print("Random Number:",a)
#To print sequence of n numbers
for a in list(range(10)):
	print("Value:",a)
b=0
for ch in 'PYTHON':
	b+=1
	print("Character:",b,ch)
for x in range(0,101,5):
	print("Five Multipliers:",x)	
num=int(input("Enter the number:"))
if num%2==0:
	print("This is Even number")
else:
	print("This is Odd Number")
a=10
while a>0:
	print("Decrement:",a)
	a-=1

