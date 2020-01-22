#!/usr/bin/env python
# coding: utf-8

# In[1]:


#tuple 2>create a tuple diff data types
var1=(1,"lk",False)
print(var1)


# In[2]:


#1>ceate empty tuple
var1=( )
print(var1)


# In[3]:


#3>print one no
var1=(10,20,30)
print(var1[1])


# In[3]:


#4>several variables
var1=(10,20,30)
a,b,c=var1
print(a,"",b,c)


# In[2]:


#5>add an item in tuple
var1=(10,20,30)
var1=var1+(40,)
print(var1)


# In[9]:


#6>converta a tuple to string
var1=("10","20","30")
str=' '.join(var1)
print(str)


# In[11]:


#7>to get 4th element
var1=("a","b","c","d","e","f","g","h")
print(var1[3]+var1[-4])


# In[13]:


#9>to find the repeated items
var1=(1,1,2,3)
print(var1.count(1))


# In[27]:


#10>element exist in a tuple
var1=(4,1,2,3)
if(var1=='5'):
    print("present")
else:
    print("absent")


# In[15]:


#11>convert a list into tuple
list1=[1,2,3,4]
var1=tuple(list1)
print(var1)


# In[20]:


#12>remove an item from a tuple
var1=(1,2,3,4)
list1=list(var1)
list1.remove(3)
var1=tuple(list1)
print(var1)


# In[34]:


#13>slice a tuple
var1=(1,2,3,4)
print(var1[2:4])


# In[31]:


#14>find an index of an item
var1=(40,10,20,3)
print(var1.index(10))


# In[32]:


#15>length of a tuple
var1=(10,20,30,40)
print(len(var1))


# In[37]:


#reverse of a tuple
var1=(10,20,30,40)
var2=reversed(var1)
print(tuple(var2))


# In[41]:





# In[ ]:




