#!/usr/bin/env python
# coding: utf-8

# # section 8: Built-Ins:  
# 
# ### writer : Faranak Alikhah 1954128

# ### 3.ginortS :
# 
# 

# In[ ]:


S=str(input()) # we can eithr sort our string here or at the end
lower=[]
upper=[]
odd=[]
even=[]
for i in S:
    if i.islower():
        lower.append(i)
    elif i.isupper():
        upper.append(i)
    elif int(i)%2 !=0:
        odd.append(i)
    elif int(i)%2==0:
        even.append(i)

lower.sort()
upper.sort()
odd.sort()
even.sort()
S_final=lower+upper+odd+even
print(*S_final ,sep='')


# 
