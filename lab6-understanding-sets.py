#!/usr/bin/env python
# coding: utf-8

# In[1]:


#create a set
set1={"a","b","c"}
set1


# In[2]:


#add an element to set
set1.add(1)
set1


# In[3]:


# adding multiple items using update function
set1.update([100,'a','$',"apple"])
set1


# In[4]:


#length of a aset
x=len(set1)
x


# In[5]:


# you can use discard function as well to remove a value from set set1.discard(100)
set1.remove(100)
set1


# In[6]:


#pop an element from set
p=set1.pop()
p


# In[7]:


#clear a set or remove all the items from set
set1.clear()
set1


# In[8]:


#delete a set
del set1
set1


# In[9]:


#union of a set
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)


# In[10]:


#update a set
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
set1


# In[11]:


#finding intersection of a set
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)
print(z)


# In[12]:


#issubset
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)
print(z)


# In[13]:


#isuperset
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

z = x.issuperset(y)
print(z)


# In[14]:


#symetric differecne
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)
print(z)


# In[ ]:


#set difference
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)
print(z)

