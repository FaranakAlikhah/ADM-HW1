#!/usr/bin/env python
# coding: utf-8

# # *section 2: Basic Data Type*
# 
# ### writer : Faranak Alikhah 1954128

# ### 2.Find the Runner-Up Score! :
# 

# In[ ]:


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    my_arr=set(arr)
    s=sorted(my_arr)
    print(s[-2])


# 
