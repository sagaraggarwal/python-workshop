#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1.	Write a program to multiply two numbers using functions.
def mul(a,b):
    c=a*b
    return(c)

a=int(input("num1"))
b=int(input("num2"))
c=mul(a,b)
print (c)


# In[2]:


# 2.	Write a program to add two numbers using functions.
def add(a,b):
    c=a+b
    return(c)

a=int(input("num1"))
b=int(input("num2"))
c=add(a,b)
print (c)


# In[3]:


#3.Calculate factorial of a number using function.
def fact(n):
    fact=1;
    for i in range(n,0,-1):
        fact=fact*i
    return (fact)
a=int(input())
b=fact(a)
print(b)


# In[4]:


#4.	Create sequence of Fibonacci using function.
def fibonacci(n):
    k=1
    a=1
    b=1
    print(a, end=" ")
    print(b, end=" ")
    while(k<=n):
        if n==1:
            return(0)
        elif n==2:
            return(1)
        else:
            c=a+b
            print(c,end=" ")
            a=b
            b=c
            k=k+1
            
a=int(input())
fibonacci(a)


# In[5]:


#5.	Write a program to swapping of two numbers using functions.
a=int(input())
b=int(input())
def swap(m,n):
    temp=m
    m=n
    n=temp
    return(m,n)
result=swap(a,b)
print(result)


# In[6]:


#6.	Write a function to find the HCF of some given numbers.
def compute_hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

num1 = int(input(" Please Enter the First Number : ")) 
num2 = int(input(" Please Enter the Second Number : "))

print("The H.C.F. is", compute_hcf(num1, num2))


# In[7]:


#7.	Write a function to find the ASCII value of the character.
c = (input(" Please Enter the Alphabet : ")) 
print("The ASCII value of '" + c + "' is", ord(c))


# In[8]:


#8.	Write a program that demonstrates the (built in function) mathematical functions.
abs(-7)


# In[9]:


#9.	Write a program that demonstrates the (built in function) Date & Time functions.
import datetime 
from datetime import date  
print ("Present date is : ",end="") 
print (date.today())


# In[10]:


#10.	Write a program that demonstrates Required arguments.
def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return;

# Now you can call printme function
printme("calling function 1st time")
printme("calling function 2nd time")


# In[11]:


# 11.	Write a program that demonstrates keyword arguments.
def student(firstname, lastname):  
     print(firstname, lastname)  
    
    
# Keyword arguments                   
student(firstname ='student1', lastname ='stdent1_ln')     
student(lastname ='student2_ln', firstname ='Student1')


# In[12]:


# 12.	Write a program that demonstrates Default arguments.
def myFun(x, y=500): 
    print("x: ", x) 
    print("y: ", y) 
  
myFun(100)


# In[13]:


# 13.	Write a program that demonstrates Variable –length arguments.  
# *args for variable number of arguments 
def myFun(*argv):  
    for arg in argv:  
        print (arg) 
    
myFun('lab', 'exercise', 'for', 'python')


# In[ ]:




