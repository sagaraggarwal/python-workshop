#!/usr/bin/env python
# coding: utf-8

# In[1]:


#2.>leap year
y=eval(input('enter the year'))
if(y%100==0):
    if(y%400==0):
        print('It is a leap year')
    else:
        print('it is not a leap year')
else:
    if(y%4==0):
        print('It is a leap year')
    else:
        print('it is not a leap year')


# In[2]:


#1.>even odd
num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")
    


# In[1]:


#3.>vowel or consonants
n=str(input("enter any alphabet:"))
if(n=='a'or n=='e'or n=='i'or n=='i'or n=='u'):
    print("vowels")
else:
    print("consonats:"+n)


# In[3]:


#5.>factorial of an no
n=int(input("enter any no.:"))
fact=1
if(n<0):
    print("factorial not possible")
elif(n==0):
    print("factorial of 0 is 1")
else:
        for i in range(1,n+1):
            
            fact=fact*i

            print("factorial of",n,"is",fact)
            


# In[5]:


#6.>print this pattern
print('    '+"*")
print('   '+"*"+' '+"*")
print('  '+"*"+' '+"*")
print(' '+"*"+"*"+' '+"*"+''+"*")


# In[6]:


#8.>prime no.
n=int(input("enter any no.:"))
if n>1:
    for i in range (2,n):
        if(n%i)==0:
            print(n,"not a prime no.")
            break
        else:
            print("it is a prime no")
        
            


# In[7]:


#9.>calculator
n1=eval(input('enter the first no.'))
n2=eval(input('enter the second no.'))
print('select a opertor (+,-,*,/,//,%,**)')
op=input('enter the above operator')
if(op=='+'):
        print(n1+n2)
elif(op=='-'):
        print(n1 - n2)
elif(op=='*'):
        print(n1*n2)
elif(op=='/'):
        print(n1/ n2)
elif(op=='//'):
        print(n1 //n2)
elif(op=='%'):
        print(n1 %n2)
elif(op=='**'):
        print(n1 **n2)
else:
        print('enter a valid operator')


# In[8]:


#4.>smallest of two no.s
n1=eval(input('enter the first no.'))
n2=eval(input('enter the second no.'))
if(n1<n2):
    print("n1 is smallest")
else:
    print("n2 is smallest")


# In[ ]:




