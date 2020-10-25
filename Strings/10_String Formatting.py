#!/usr/bin/env python
# coding: utf-8

# # *section 3: Strings*
# 
# ### writer : Faranak Alikhah 1954128

# ### 10. String Formatting :
# 

# In[ ]:


def print_formatted(number):
    # your code goes here
    bl=len("{0:b}".format(number))
    for i in range(1,number+1):
         print("{0:{bl}d}".format(i,bl=bl), "{0:{bl}o}".format(i,bl=bl), "{0:{bl}X}".format(i,bl=bl), "{0:{bl}b}".format(i,bl=bl),sep=" ")


# 
