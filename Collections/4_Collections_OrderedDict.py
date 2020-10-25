#!/usr/bin/env python
# coding: utf-8

# # section 5: Colloctions  
# 
# ### writer : Faranak Alikhah 1954128

# ### 4.Collections.OrderedDict:
# 
# 

# In[ ]:


from collections import OrderedDict
n=int(input())
name_price=OrderedDict()
for i in range (n):
    a=input().split()
    item_name=' '.join(a[:-1])
    item_price=int(a[-1])
    if item_name in name_price:
        name_price[item_name] += item_price
    else:
        name_price[item_name]=item_price

for item_name,item_price in name_price.items():
    print(item_name,item_price)


# 
