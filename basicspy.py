#print() function
a=50
b="Sample"
c='M'
d=120
print(a,b,c,d)
place="Chennai"
print(place*5)
print(place[4])
print(place[-6])
print(place[2:5])
print(len(place))
e=a+d
print(e)
f=a/d
print(f)
g=a*d
print(g)
h=a**d
#////////////////////list Example
li=[10,20,30,40,100]
print(li)
li2=[100,"Sample",'Text']
print(li2)
print(li+li2)
combo=li+li2
print(combo)
print(combo[3:6])
#//////////////////////tuple
lis=(10,20,40)
print(lis)
print(lis[2])
#lis[2]=33 is not supported
tup=('Value',10)
print(tup)
#///////////////////////dic
dict={'Name':'Vignesh','Course':'B.Tech'}
print(dict)
print(dict.keys())
#///////////////////functions
print(set(li)&set(li2))
print(dict.values())
print("Intersection is :",set(li).intersection(li2))
print("Union is:",set(li).union(li2))
print(bool(set(li)&set(li2)))
list1=list(lis)
print(list1)
