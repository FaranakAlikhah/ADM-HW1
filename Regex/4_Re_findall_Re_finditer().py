#!/usr/bin/env python
# coding: utf-8

# # section 13.Regex and Parsing challenges :  
# 
# ### writer : Faranak Alikhah 1954128

# ### 4.Re.findall() & Re.finditer() :

# In[ ]:


import re
vowel ='aeiou'
consonant ='qwrtypsdfghjklzxcvbnm'
match = re.findall(r'(?<=['+consonant+'])(['+vowel+']{2,})(?=['+consonant+'])', input(),flags=re.I)
print('\n'.join(match or ['-1']))


# 
