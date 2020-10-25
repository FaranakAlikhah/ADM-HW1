#!/usr/bin/env python
# coding: utf-8

# # section 12. Numpy :  
# 
# ### writer : Faranak Alikhah 1954128

# ### 8. Floor, Ceil and Rint :

# In[ ]:


import numpy

arr=input().strip().split()
arr=numpy.array(arr,float)
numpy.set_printoptions(sign=' ')
print (numpy.floor(arr))
print (numpy.ceil(arr))
print (numpy.rint(arr))


# 
