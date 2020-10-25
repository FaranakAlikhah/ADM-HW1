#!/usr/bin/env python
# coding: utf-8

# # *section 2: Basic Data Type*
# 
# ### writer : Faranak Alikhah 1954128

# ### 5. Tuples :
# 

# In[ ]:


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t=tuple(integer_list)
    print (hash(t))


# 
