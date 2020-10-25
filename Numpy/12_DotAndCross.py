#!/usr/bin/env python
# coding: utf-8

# # section 12. Numpy :  
# 
# ### writer : Faranak Alikhah 1954128

# ### 12. Dot and Cross :

# In[ ]:


import numpy

N = int(input())
a = numpy.array([input().split() for i in range(N)], int)
b = numpy.array([input().split() for i in range(N)], int)
print(numpy.dot(a,b))


# 
