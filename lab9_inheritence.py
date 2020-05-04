#!/usr/bin/env python
# coding: utf-8

# In[1]:


#SIMPLE INHERITENCE
class Person:
    person_name=""
    employee_name=""
    def disp_person(self):
        print(self.person_name)
class Employee(Person):
    def disp_employee(self):
        print(self.employee_name)
emp1=Employee()
emp1.person_name="par"
emp1.employee_name="abc"
emp1.disp_employee()


# In[ ]:


# print values of the function using object
emp1.disp_employee()


# In[ ]:


#display variable of a class from object
class A:
    x=""
    def disp(self):
        print(x)
class B:
    def prnt(self):
        print(p)
o=B()
o.p="post"
print(o.p)


# In[5]:


#multilevel inheritence
class Person:
    person_name=""
    employee_name=""
    teacher_name=""
    def disp_person(self):
        print(self.person_name)
class Employee(Person):
    def disp_employee(self):
        print(self.employee_name)
class Teacher(Employee):
    def disp_teacher(self):
        print(self.teacher_name)
obj1=Teacher()
obj1.person_name="par"
obj1.employee_name="abc"
obj1.teacher_name="tea"
obj1.disp_person()


# In[1]:


# hierarical inheritance
class Person:
    person_name=""
    member_name=""
    def disp_person(self):
        print(self.person_name)
# do not forget to write in argument of child class
class Employee(Person):
    def disp_member(self):
        print(self.member_name)
class Student(Person):
    def disp_member(self):
        print(self.member_name)
emp1=Employee()
emp1.person_name="par"
emp1.member_name="abc_emp"
emp1.disp_person()


# In[2]:


emp1.disp_member()


# In[ ]:


stu1=Student()
stu1.person_name="par"
stu1.member_name="def_stu"
stu1.disp_person()


# In[3]:


stu1.disp_member()


# In[4]:


#multiple level inheritence
class A:
    A_name=""
    def disp_A(self):
        print(self.person_name)
class B:
    B_name=""
    def disp_B(self):
            print(self.member_name)
class C(A,B):
    def disp_C(self):
        print(self.A_name,self.B_name)
ob1=C()
ob1.A_name="a"
ob1.B_name="b"
ob1.disp_C()


# In[5]:


#inheritance using constructor
# user __init__ function to create a constructor
# self is used similar to 'this' java operator in Python 
#to represent linking of variables with an object

class Base:
    def __init__(self,name):
        self.name=name

class Derived(Base):
    def __init__(self,name, roll_no):
        Base.__init__(self,name)
        self. roll_no=roll_no
ob1=Derived("xyz",24)
print(ob1.roll_no, ob1.name)


# In[ ]:




