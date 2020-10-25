#!/usr/bin/env python
# coding: utf-8

# # section 5: Colloctions  
# 
# ### writer : Faranak Alikhah 1954128

# ### 5.Word Order :
# 
# 

# In[ ]:


from collections import Counter
a=list()
for i in range(int(input())):
    a.append(input())

num=Counter(a) #output of vounter is dictionary
print(len(num))
print(*num.values())
#second way :
# for i in num.values()
#     print(i,end=" ")


# 
