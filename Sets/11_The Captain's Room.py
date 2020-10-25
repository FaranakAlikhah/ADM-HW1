#!/usr/bin/env python
# coding: utf-8

# # *section 4: Strings*
# 
# ### writer : Faranak Alikhah 1954128

# ### 11. The Captain's Room:
# 
# 

# In[ ]:


size_group=input()
rooms_num=list(map(int,input().split()))
test1=set()
test2=set()
for i in rooms_num:
    if i not in test1:
        test1.add(i)
        test2.add(i)
    else:
        test2.discard(i)
test2=list(test2)
print(*test2)


# 
