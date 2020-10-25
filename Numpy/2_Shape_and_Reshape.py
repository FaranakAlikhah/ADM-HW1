#!/usr/bin/env python
# coding: utf-8

# # section 12. Numpy :  
# 
# ### writer : Faranak Alikhah 1954128

# ### 2.Shape and Reshape :
# 
# 

# In[ ]:


import numpy


arr = list(map(int,input().split()))
my_array = numpy.array(arr)
print (numpy.reshape(my_array,(3,3)))


# 
