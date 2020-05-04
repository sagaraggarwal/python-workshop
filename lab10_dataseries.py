#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


#empty Series
s = pd.Series()
print(s)


# In[3]:


# series from an array
data = np.array(['a','b','c','d'])
s = pd.Series(data)
print(s)


# In[4]:


# giving user defined index to series
data = np.array(['a','b','c','d'])
s = pd.Series(data,index=[107,101,102,103])
print(s)


# In[5]:


# creating series using dictionary
data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data)
print(s)


# In[6]:


# giving index to series
data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data,index=['b','c','d','a'])
print(s)


# In[7]:


# series from scalar values
s = pd.Series(5, index=[10, 11, 12, 13])
print (s)


# In[9]:


# Accesssing data
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print(s)
#retrieve the first element
print (s[0])

#retrieve a single element using index
print (s['a'])

#retrieve the first three element
print (s[:3])

#retrieve multiple elements
print (s[['a','c','d']])


# In[10]:


df = pd.DataFrame()
print(df)


# In[11]:


#dataframe using list
data = [1,2,3,4,5]
df = pd.DataFrame(data)
print(df)


# In[13]:


# creating two columns
data = [['rohit',10],['birbal',12],['drishtadyumn',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print (df)


# In[14]:


# giving float values
data = [['rohit',10],['Birbal',12],['drishtadyumn',13]]
df = pd.DataFrame(data,columns=['Name','Age'],dtype=float)
print (df)


# In[16]:


# dataframe using dictionary
data = {'Name':['bheem', 'nakul', 'sahdev', 'arjun'],'Age':[28,34,29,42]}
df = pd.DataFrame(data)
print (df)


# In[18]:


# creating index
data = {'Name':['bheem', 'nakul', 'sahdev', 'arjun'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['roll1','roll2','roll3','roll4'])
print (df)


# In[19]:


# dataframe from multiple dictionaries
#understanding Nan
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print (df)


# In[20]:


# Dataframe from Series
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print (df)


# In[21]:


# selecting a column
print (df['one'])


# In[22]:


# add a third column
df['three']=pd.Series([10,20,30],index=['a','b','c'])
print (df)


# In[23]:


# delete a cloumn
print ("Deleting the first column using DEL function:")
del df['three']
print (df)


# In[24]:


# selecting row from data frame
print (df.iloc[2])
#print (df.iloc['b']) # will give error as iloc indicate index location .
# use loc instead
print (df.loc['b'])


# In[25]:


# slicing
df = pd.DataFrame(d)
print (df[2:4])


# In[26]:


# adding rows
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])
df = df.append(df2)
print (df)
# try chainging 'a' and 'b' with 'one' and 'two'


# In[27]:


# deleting row 
df = df.drop('a')
print(df)


# In[ ]:




