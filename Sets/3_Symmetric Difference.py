#!/usr/bin/env python
# coding: utf-8

# # *section 4: Strings*
# 
# ### writer : Faranak Alikhah 1954128

# ### 3.Symmetric Difference :
# 

# In[ ]:


M=int(input())
a=set(map(int,input().split()))
N=int(input())
b=set(map(int,input().split()))
print(*sorted(a^b),sep='\n')


# 
