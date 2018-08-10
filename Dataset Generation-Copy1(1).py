
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


import numpy as np


# In[4]:


from random import *


# In[7]:


index=np.arange(1,2001)


# In[13]:


print(index)


# In[8]:


speed=[]
no_of_persons=[]


# In[14]:


for var in list(range(2000)):
    speed.append(round(np.random.uniform(2,8), 2))
    no_of_persons.append(randint(1000, 10000))
print(no_of_persons)    
print(speed)    


# In[10]:


raw={'Index':index,'Speed_Mbps':speed,'No_Of_Persons':no_of_persons}


# In[11]:


df=pd.DataFrame(raw,columns=['Index','Speed_Mbps','No_Of_Persons'])


# In[12]:


df.to_csv('Dataset.csv')

