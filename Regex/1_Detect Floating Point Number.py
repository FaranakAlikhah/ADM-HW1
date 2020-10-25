#!/usr/bin/env python
# coding: utf-8

# # section 13.Regex and Parsing challenges :  
# 
# ### writer : Faranak Alikhah 1954128

# ### 1. Detect Floating Point Number :

# In[ ]:


import re

pattern = r'^[-+]?[0-9]*\.[0-9]+$'
#^ Complements a character class
#+ Matches one or more repetitions
#- negative numbers
# * Matches zero or more repetitions
# \  Escapes a metacharacter of its special meaning-Introduces a special character
#      class-Introduces a grouping backreference
# $  Anchors a match at the end of a string
for i in range(int(input())):
    s=input()
    print(bool(re.match(pattern,s)))

# Since I had no idea bout this concept I tried to read different solutions and notes
# also I store other kinda solutions that were readable and understandable to me and try to learn them
#from re import match, compile
#pattern = compile('^[-+]?[0-9]*\.[0-9]+$')
#for _ in range(int(input())):
    #print(bool(pattern.match(input())))


# 
