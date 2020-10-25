#!/usr/bin/env python
# coding: utf-8

# # section 12. Numpy :  
# 
# ### writer : Faranak Alikhah 1954128

# ### 7. Array Mathematics :

# In[ ]:


import numpy
N, M = list(map(int, input().split()))

a = numpy.array([input().split() for i in range(N)], int)
b = numpy.array([input().split() for i in range(N)], int)
print(numpy.add(a, b))
print(numpy.subtract(a, b))
print(numpy.multiply(a, b))
print(numpy.array(a/b,int))
print(a%b)
print(a**b)


# 
