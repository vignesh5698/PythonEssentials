def a():
	try:
		a=int(input("Enter number:"))
		b=int(input("Enter Divisior:"))
		c=a/b
		print(c)
	except ZeroDivisionError:
		print("Divide by Zero Error.........")
	except TypeError:
		print("Type Error Buddyyy....")
	except ImportError:
		print("Import Errorr.....")
a()
