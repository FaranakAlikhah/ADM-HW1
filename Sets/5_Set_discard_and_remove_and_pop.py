#!/usr/bin/env python
# coding: utf-8

# # *section 4: Strings*
# 
# ### writer : Faranak Alikhah 1954128

# ### 4.Set .discard(), .remove() & .pop():
# 

# In[ ]:


n = int(input())
s = set(map(int, input().split()))
num_comments=int(input())
for i in range(num_comments):
    comments=input().split( )
    if comments[0]=="remove":
            s.remove(int(comments[1]))
    elif comments[0]=="discard":
            s.discard(int(comments[1]))
    else :
         s.pop()

         
print(sum(s))


# 
