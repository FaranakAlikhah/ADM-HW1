#!/usr/bin/env python
# coding: utf-8

# # section 13.Regex and Parsing challenges :  
# 
# ### writer : Faranak Alikhah 1954128

# ### 6. Validating Roman Numerals :

# In[ ]:


f = 'M{0,3}'
s = '(C[MD]|D?C{0,3})'
t = '(X[CL]|L?X{0,3})'
l = '(I[VX]|V?I{0,3})'
regex_pattern = f+s+t+l+'$' 


# 
