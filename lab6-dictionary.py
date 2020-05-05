#!/usr/bin/env python
# coding: utf-8

# In[7]:


dict1={
    "A":1,
    "B":2,
    "C":3,
    "D":4,
    
}
for key in dict1:
    print(key)
    for key,value in dict1.items():
        print(key,value)
        for key,value in dict1.items():
            print(value)


# In[8]:


dict1={
    "Mango":"Fruit"
    "Apple":"Fruit"
    "Potato":"Vegetable"
    "Tomato":"Vegetable"
}
if "Mango" in dict1:
    print()


# In[11]:


dict1={
    "A":1,
    "B":2,
    "C":3,
}
    print(dict1)
    dict1['A']=4
    print(dict1)


# In[1]:


dict1={
    "A":1,
    "B":2,
    "C":3,
}
dict2={
    "A":7,
    "B":4,
    "C":5,
}
cmp(dict1,dict2)


# In[17]:


dict1={
    "A":12,
     1:"ABC",
    5:{"A":16,
     2:"DEF"},
    "C":17
    
}
print(dict1)


# In[24]:



dict1={
    "A":1,
    "B":2,
    "C":3,
}
dict2={
    "A":7,
    "E":4,
    "F":5,
}
dict3={
    "G":8,
    "H":9,
    }
d4={}
for d in (dict1,dict2,dict3):
      d4.update(d)
print(d4)


# In[2]:


# finding sum total of all the values in a dictionary
dict1={}
for key in range(1,11):
    dict1[key]=key*key
    print(dict1)
sum(dict1)


# In[ ]:




