#!/usr/bin/env python
# coding: utf-8

# # section 12. Numpy :  
# 
# ### writer : Faranak Alikhah 1954128

# ### 10. Min and Max:

# In[ ]:


import numpy

N,M = map(int,input().split())
a = numpy.array([input().split() for i in range(M)], int)
print(numpy.max(numpy.min(a, axis = 1)))


# 
