#!/usr/bin/env python
# coding: utf-8

# # section 12. Numpy :  
# 
# ### writer : Faranak Alikhah 1954128

# ### 15. Linear Algebra :

# In[ ]:


import numpy

N=int(input())
A = numpy.array([input().split() for i in range(N)], float)

numpy.set_printoptions(legacy='1.13') #important
print(numpy.linalg.det(A))


# 
