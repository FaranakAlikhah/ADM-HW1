#!/usr/bin/env python
# coding: utf-8

# # section 12. Numpy :  
# 
# ### writer : Faranak Alikhah 1954128

# ### 11. Mean_Var_Std :

# In[ ]:


import numpy

N,M = map(int,input().split())
a = numpy.array([input().split() for i in range(M)], int)
numpy.set_printoptions(legacy='1.13')
# or numpy.around(decimal=11)
print(numpy.mean(a, axis = 1))
print(numpy.var(a, axis = 0))
print(numpy.std(a))


# 
