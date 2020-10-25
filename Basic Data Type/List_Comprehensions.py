#!/usr/bin/env python
# coding: utf-8

# # *section 2: Basic Data Type*
# 
# ### writer : Faranak Alikhah 1954128

# ### 1.List Comprehensions :
# 

# In[ ]:


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
my_list=[[i,j,k] for i in range (0,x+1) for j in range(0,y+1) for k in range (0,z+1) if i+j+k != n]
print(my_list)


# 
