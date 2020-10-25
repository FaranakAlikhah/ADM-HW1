#!/usr/bin/env python
# coding: utf-8

# # section 7: Exceptions :  
# 
# ### writer : Faranak Alikhah 1954128

# ### 1.Exceptions :
# 
# 

# In[ ]:


n=int(input())
for i in range(n):
    try: 
        a,b=map(int,input().split())
        print(a//b)# need to be integer
    except Exception as e:
         print ("Error Code:",e)


# 
