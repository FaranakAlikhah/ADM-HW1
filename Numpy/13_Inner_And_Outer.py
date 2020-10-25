#!/usr/bin/env python
# coding: utf-8

# # section 12. Numpy :  
# 
# ### writer : Faranak Alikhah 1954128

# ### 13. Inner And Outer :

# In[ ]:


import numpy

A=list(map(int,input().split()))
B=list(map(int,input().split()))
print (numpy.inner(A, B))
print (numpy.outer(A, B))


# 
