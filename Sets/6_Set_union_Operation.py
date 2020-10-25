#!/usr/bin/env python
# coding: utf-8

# # *section 4: Strings*
# 
# ### writer : Faranak Alikhah 1954128

# ### 6.Set .union() Operation :
# 

# In[ ]:


n=int(input())
english_student=set(map(int,input().split()))
b=int(input())
french_student=set(map(int,input().split()))
print(len(french_student.union(english_student)))


# 
