#!/usr/bin/env python
# coding: utf-8

# # *section 4: Strings*
# 
# ### writer : Faranak Alikhah 1954128

# ### 12.Check Subset:
# 
# 

# In[ ]:


num_testCase=int(input())
for i in range(num_testCase):
    num_testCase1=int(input())
    a=set(input().split())
    num_testCase2=int(input())
    b=set(input().split())
    print(a.issubset(b))


# 
