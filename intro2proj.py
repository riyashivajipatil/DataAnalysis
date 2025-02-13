#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("hi")


# In[4]:


import pandas as pd


# In[7]:


data=pd.read_csv(r'C:\Users\Riya Shivaji Patil\Downloads\Heart (1).csv')


# In[8]:


data


# In[9]:


print(data)


# In[10]:


print(data.head())


# In[11]:


print(data.tail())


# In[12]:


data.tail()


# In[13]:


data.describe()


# In[14]:


data.info()


# In[15]:


import numpy as np


# In[16]:


data.isnull()


# In[18]:


print(data.isnull().sum())


# In[20]:


data.info()


# In[21]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[22]:


import plotly.express as px


# In[23]:


xpoints=np.array([0,6])
ypoints=np.array([0,250])


# In[24]:


plt.plot(xpoints,ypoints)
plt.show()


# In[25]:


plt.plot(xpoints,ypoints,'o')
plt.show()


# In[31]:


import matplotlib.pyplot as plt


# In[42]:


xpoints=np.array([1,2,3])
ypoints=np.array([50,100,150])


# In[43]:


plt.plot(xpoints,ypoints)
plt.show()


# In[46]:


a=np.array([90,90])


# In[47]:


plt.pie(a)
plt.pie()


# In[49]:


x=np.random.normal(170,10,250)
print (x)


# In[50]:


plt.hist(x)
plt.show()


# In[54]:


sns.displot([0,1,2,3,4,5])


# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.metrics import mean_squared_error,r2_score

# In[55]:


from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestRegressor 
from sklearn.metrics import mean_squared_error,r2_score



# In[ ]:


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)

