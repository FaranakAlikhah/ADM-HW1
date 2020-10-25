#!/usr/bin/env python
# coding: utf-8

# # section 13.Regex and Parsing challenges :  
# 
# ### writer : Faranak Alikhah 1954128

# ### 3. Group(), Groups() & Groupdict() :

# In[ ]:


import re 
s= input()
pattern=r'([A-Z a-z 0-9])\1+'#alphabet numeric 
m=re.search(pattern,s)
if m:
    print(m.group(1))
else:
    print(-1)


# 
