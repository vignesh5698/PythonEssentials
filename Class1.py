#Function And Class Example
a=input("Enter the Name:")
b=int(input("Enter PassWord:"))
a1=[]
def operation():

	print("1.Insert \n2.View\n3.Calculate")
	choice=input("Enter your Choice:")
	if choice=="1":
		b=int(input("Enter Number of Students:"))
#		a1=[]
		n=0
		while b>0:
		        a1.insert(n,input("Enter the Name:"))
		        print("Student",n+1,"Inserted")
		        n=n+1
		        b=b-1
	elif choice=="2":
		if len(a1) != 0:
			for name in a1:
				print(name)

		else:
			print("No Data...")
if a=="vikki" and b == 1234:
	print("Valid User")
	operation()
	x1='y'
	x=input("Do You Want To Continue? y=YES n=NO")
	while x1==x:
		operation()
		print("Do you want to continue operation..?")
	
else:
	print("Invalid User:")

