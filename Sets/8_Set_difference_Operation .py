#!/usr/bin/env python
# coding: utf-8

# # *section 4: Strings*
# 
# ### writer : Faranak Alikhah 1954128

# ### 8.Set .difference() Operation :
# 

# In[ ]:


n=int(input())
english_student=set(map(int,input().split()))
b=int(input())
french_student=set(map(int,input().split()))
print(len(english_student.difference(french_student)))


# 
