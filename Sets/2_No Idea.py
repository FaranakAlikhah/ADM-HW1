#!/usr/bin/env python
# coding: utf-8

# # *section 4: Strings*
# 
# ### writer : Faranak Alikhah 1954128

# ### 2.No Idea! :
# 

# In[ ]:


n=[map(int,input().split())]
arr=map(int,input().strip().split())
A =set( map(int,input().split()))
B =set( map(int,input().split()))
A_counter=0
B_counter=0
happines=0
for i in arr:
    if i in A:
        happines+=1
    elif i in B:
        happines-=1

print(happines) 


# 
