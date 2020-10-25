#!/usr/bin/env python
# coding: utf-8

# # section 5: Colloctions  
# 
# ### writer : Faranak Alikhah 1954128

# ### 3.Collections.namedtuple:
# 
# 

# In[ ]:


from collections import namedtuple
num_student=int(input())
info=namedtuple("info",input().split())
total_grade=[]
for i in range(num_student):
    grade=int(info._make(input().split()).MARKS)
    total_grade.append(grade)
print((sum(total_grade)/num_student))


# 
