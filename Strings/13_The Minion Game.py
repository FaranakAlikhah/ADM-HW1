#!/usr/bin/env python
# coding: utf-8

# # *section 3: Strings*
# 
# ### writer : Faranak Alikhah 1954128

# ### 13.The Minion Game :
# 

# In[ ]:


def minion_game(string):
    vowels = ['A','E','I','O','U']
    kevin_score = 0
    stuart_score = 0
    for i in range(len(string)):
         if s[i] in vowels:
            kevin_score += len(string)-i
         else:
            stuart_score += len(string)-i
    if kevin_score > stuart_score:
          print ("Kevin {}".format(kevin_score))
    elif kevin_score < stuart_score:
          print ("Stuart {}".format(stuart_score))
    else:
          print ("Draw")


# 
