#!/usr/bin/env python
# coding: utf-8

# # *section 3: Strings*
# 
# ### writer : Faranak Alikhah 1954128

# ### 4.Mutations  :
# 

# In[ ]:


def mutate_string(string, position, character):
    string=list(string)
    string[position]=character
    string="".join(string)
    return string


# 
