#!/usr/bin/env python
# coding: utf-8

# # section 10: XML :  
# 
# ### writer : Faranak Alikhah 1954128

# ### 1.ML 1 - Find the Score :
# 
# 

# In[ ]:



def get_attr_number(node):
    # your code goes here
    a=len(node.attrib)+sum(get_attr_number(child) for child in node)
    return a


# 
