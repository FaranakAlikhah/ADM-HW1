#!/usr/bin/env python
# coding: utf-8

# # *section 3: Strings*
# 
# ### writer : Faranak Alikhah 1954128

# ### 8. Text Wrap :
# 

# In[ ]:


def wrap(string, max_width):
   result = "\n".join(string[i:i+max_width] for i in range(0,len(string),max_width))

   return result


# 
