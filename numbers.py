import random
print("Random:",random.random())
print("Random Value in int:",random.randint(1,6))
random.seed(1)
print("SEED added",random.randint(0,5))
random.seed()
print(random.random()*100)
#Choice
a=["Red","Green","Blue"]
print(random.choice(a))
#shuffle
random.shuffle(a)
print(a)
#randrange(Start,Stop,StepSize)
b=random.randrange(0,100,10)
print(b)
