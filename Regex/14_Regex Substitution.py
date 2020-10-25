#!/usr/bin/env python
# coding: utf-8

# # Exercise 1. Regex and Parsing challenges  :  
# ### writer : Faranak Alikhah 1954128

# ### 14.Regex Substitution :

# In[ ]:


for _ in range(int(input())):
    line = input()
    while '&&'in line or '||'in line:
        line = line.replace("&&", "and").replace("||", "or")
    print(line)


# 

# 
