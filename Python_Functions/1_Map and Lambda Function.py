#!/usr/bin/env python
# coding: utf-8

# # section 9: Python Functions :  
# 
# ### writer : Faranak Alikhah 1954128

# ### 1.Map and Lambda Function :
# 
# 

# In[ ]:


cube = lambda x: x**3# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    a=0
    b=1
    l=[]
    if n==0:
            l=[]
    elif n==1:
            l.append(a)
    elif n>=2:
            l.append(a)
            l.append(b)
    for i in range(2,n):
            c=a+b
            a=b
            b=c
            l.append(c)
    return l


# 
