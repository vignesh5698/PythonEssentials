import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x=np.arange(1,10)
y=x**2
plt.plot(x,y,'blue')
plt.show()
plt.plot(x,y,'r--')
plt.show()
plt.plot(x,y,'g*')
plt.show()
plt.xlim(0,10)
plt.ylim(0,10)
plt.title("MySample")
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()
mat=np.arange(0,10).reshape(5,2)
print(mat)
plt.imshow(mat,cmap='coolwarm')
plt.colorbar()
plt.show()