#!/usr/bin/env python
# coding: utf-8

# # *section 3: Strings*
# 
# ### writer : Faranak Alikhah 1954128

# ### 5.Find a string :
# 

# In[ ]:


def count_substring(string, sub_string):
    count=0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count += 1
    return count


# 
