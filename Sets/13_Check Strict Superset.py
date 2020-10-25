#!/usr/bin/env python
# coding: utf-8

# # *section 4: Strings*
# 
# ### writer : Faranak Alikhah 1954128

# ### 13.Check Strict Superset:
# 
# 

# In[ ]:


A = set(input().split())
N = int(input())

count=0
for i in range (N):
    check = set(input().split())
    if A.issuperset(check):
        count=count+1 
print(count==N)


# 
