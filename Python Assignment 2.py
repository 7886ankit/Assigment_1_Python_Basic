#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Create the below pattern using nested for loop in Python.
'''
* 

* * 

* * * 

* * * * 

* * * * * 

* * * * 

* * * 

* * 

* '''

n=int(input("Enter the number :"))
for i in range(n):
    for j in range(0,i+1):
        print("*",end=" ")
    print("\n")
for i in range(n-1,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print("\n")


# In[2]:


# Write a Python program to reverse a word after accepting the input from the user.
#sample:
'''Input word: ineuron
   Output: norueni '''
l=[]
n=input("Enter the name : ")[::-1]
l.append(str(n))
print(l)

