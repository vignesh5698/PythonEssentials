def a():
	try:
		a=int(input("Enter number:"))
		b=int(input("Enter Divisior:"))
		c=a/b
		print(c)
	except ZeroDivisionError:
		print("Divide by Zero Error.........")
	except ValueError:
		print("Value Error Buddyyy....")
	except ImportError:
		print("Import Errorr.....")
a()

print("Here we are raising exception")
def b():
	try:
		raise NameError("I think it\'s an error...")
	except NameError:
		print("Exception Occured.......")
b()

def c():
	try:
		raise KeyboardInterrupt
	finally:
		print("GOOD BYEE..........")
c()
