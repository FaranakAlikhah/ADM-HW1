#!/usr/bin/env python
# coding: utf-8

# # *section 5: Colloctions *
# 
# ### writer : Faranak Alikhah 1954128

# ### 1.collections.Counter :
# 
# 

# In[ ]:


from collections import Counter
num_shoes=int(input())
my_form=list(map(int,input().split()))
my_form=Counter(my_form)
num_customers=int(input())
earning=0
for i in range(num_customers):
    size,price=map(int,input().split())
    if my_form[size]>0:
       earning=earning+price
       my_form[size]-=1


print(earning)


# 
