#!/usr/bin/env python
# coding: utf-8

# # *section 3: Strings*
# 
# ### writer : Faranak Alikhah 1954128

# ### 12.Capitalize! :
# 

# In[ ]:


import stringprep
def solve(s):
    capit=s.split()
    for i in capit:
        s=s.replace(i,i.capitalize())
    return s


# 
