#!/usr/bin/env python
# coding: utf-8

# # Exercise 1. Regex and Parsing challenges  :  
# ### writer : Faranak Alikhah 1954128

# ### 13. Validating Credit Card Numbers  :

# In[ ]:


import re
code = re.compile(
    r"^"
    r"(?!.*(\d)(-?\1){3})"
    r"[456]"
    r"\d{3}"
    r"(?:-?\d{4}){3}"
    r"$")
for _ in range(int(input().strip())):
    print("Valid" if code.search(input().strip()) else "Invalid")


# 

# 
