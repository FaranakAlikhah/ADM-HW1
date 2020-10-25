#!/usr/bin/env python
# coding: utf-8

# # section 12. Numpy :  
# 
# ### writer : Faranak Alikhah 1954128

# ### 4.Concatenate  :

# In[ ]:


import numpy

N, M , P=list(map(int,input().split( )))

first_item=[]
second_item=[]
for i in range(N):
    a = list(map(int,input().split()))
    first_item.append(a)

for i in range(M):
    b = list(map(int,input().split()))
    second_item.append(b)
# I also learnt better way to write upper loops
# arr1=numpy.array([input().split() for i in range(N),int])
#arr2=numpy.array([input().split() for i in range(M),int])
arr1 = numpy.array(first_item)
arr2 = numpy.array(second_item)
print(numpy.concatenate((arr1,arr2),axis=0))


# 
