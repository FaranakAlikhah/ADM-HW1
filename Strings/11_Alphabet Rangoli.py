#!/usr/bin/env python
# coding: utf-8

# # *section 3: Strings*
# 
# ### writer : Faranak Alikhah 1954128

# ### 11.Alphabet Rangoli :
# 

# In[ ]:


from string import ascii_lowercase as alpha 
import string
def print_rangoli(size):
    # your code goes here
    a = string.ascii_lowercase
    shape = []
    for i in range(size):
        s = "-".join(a[i:size])
        shape.append((s[::-1]+s[1:]).center(4*size-3, "-"))
    print('\n'.join(shape[:0:-1]+shape))


# 
