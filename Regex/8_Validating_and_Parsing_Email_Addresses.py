#!/usr/bin/env python
# coding: utf-8

# # section 13.Regex and Parsing challenges :  
# 
# ### writer : Faranak Alikhah 1954128

# ### 8.Validating and Parsing Email Addresses :

# In[ ]:


import re
n=input()
for i in range(int(n)):
    name,email=input().split(" ")
    pat="<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>"
    if bool(re.match(pat,email)):
        print(name,email)


# 
