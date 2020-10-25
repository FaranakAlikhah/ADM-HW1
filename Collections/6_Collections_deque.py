#!/usr/bin/env python
# coding: utf-8

# # section 5: Colloctions  
# 
# ### writer : Faranak Alikhah 1954128

# ### 6.Collections.deque :
# 
# 

# In[ ]:


from collections import deque
num_op=int(input())
d=deque()
for i in range (num_op):
    comments=input().split()
    if comments[0]=='append':
        d.append(comments[1])
    elif comments[0]=='pop':
        d.pop()
    elif comments[0]=='appendleft':
        d.appendleft(comments[1])
    else :
        d.popleft()

print(*d)


# 
