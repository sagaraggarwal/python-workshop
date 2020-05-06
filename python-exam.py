#!/usr/bin/env python
# coding: utf-8

# In[1]:


#THEORITICAL QUESTIONS
#Q1. What is the syntax to call a constructor of a base class from child class
# Ans= we can call using super() Command.
#Q2:  How is a class made as inherited class (syntax of child class) 
#Ans class Parent:
 #    pass
#class Child(Parent):
 #    pass
     #Here the class child inherits the class parent
#Q3:Print an element of a nested dictionary
#people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
 #         2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}
#print(people)


# In[8]:


#SET-A
#Q1 Write a program, which will find all such numbers between 1000 and 3000 (both included)
#such that each digit of the number is an even number.
items=[]
for i in range(1000,3000):
    s=str(i)
    if(int (s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
       items.append(s)
print(",".join(items))


# In[10]:


#Q2 Define a function that can receive two integral numbers in string form and compute their sum and then print it in console.
def calculateSum(a,b):
    s=int(a)+int(b)
    return s
#main code
#to take two no as strings
num1="30"
num2="40"

sum=calculateSum(num1,num2)
print("sum =",sum)


# In[ ]:




