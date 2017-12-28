
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


li=[12,23,34,45,56,67,78,89,90]


# In[4]:


print(np.array(li))


# In[5]:


print(np.arange(0,100))


# In[6]:


print(np.arange(0,100,5))


# In[8]:


print(np.ones((4,4)))


# In[9]:


print(np.linspace(0,10,3))


# In[12]:


print(np.random.randint(1,100,150))


# In[13]:


np.random.seed(1)


# In[23]:


np.random.seed(13)
print(np.random.randint(1,30))


# In[27]:


a=np.random.randint(1,100,100)
b=a.reshape(10,10)


# In[30]:


print(b)


# In[31]:


import pandas as pd


# In[32]:


df=pd.read_csv("Documents/test.csv")


# In[33]:


print(df)


# In[34]:


print(df.describe)


# In[37]:


print(df[df['Marks']>50])


# In[38]:


print(df['Marks']<50)


# In[39]:


print(df[df['Marks']<50])


# In[42]:


import matplotlib.pyplot as plt


# In[43]:


x=np.arange(1,10)


# In[44]:


y=x**2


# In[45]:


plt.plot(x,y,'blue')


# In[46]:


plt.plot(x,y,'*')


# In[47]:


plt.plot(x,y,'p')


# In[48]:


plt.plot(x,y,'M')


# In[53]:


mat=np.arange(0,900).reshape(30,30)


# In[54]:


print(mat)


# In[55]:


mat2=mat**2


# In[57]:


plt.plot(mat,mat2,'*')

