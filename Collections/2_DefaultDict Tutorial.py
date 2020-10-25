#!/usr/bin/env python
# coding: utf-8

# # section 5: Colloctions  
# 
# ### writer : Faranak Alikhah 1954128

# ### 2.DefaultDict Tutorial :
# 
# 

# In[ ]:


from collections import defaultdict
n,m=map(int,input().split())
my_D=defaultdict(list) 
for i in range(n):
    # I leart .rstrip from one video that I watched because I am supper beginner
    char=input().rstrip()
    my_D[char].append(i+1) 
    
for i in range(m):
    char_check=input().rstrip()
    if char_check in my_D:
        print(' '.join(map(str,my_D[char_check])))
    else :
        print('-1')


# 
