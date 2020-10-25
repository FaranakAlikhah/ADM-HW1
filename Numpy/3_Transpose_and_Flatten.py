#!/usr/bin/env python
# coding: utf-8

# # section 12. Numpy :  
# 
# ### writer : Faranak Alikhah 1954128

# ### 3.Transpose and Flatten  :

# In[ ]:


import numpy
m,n=map(int,input().split())
l=[]
for i in range(m):
    k=input().split()
    l.append(k)

my_array = numpy.array(l,int)
print (numpy.transpose(my_array))
print(my_array.flatten())


# 
