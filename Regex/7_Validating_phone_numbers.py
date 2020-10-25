#!/usr/bin/env python
# coding: utf-8

# # section 13.Regex and Parsing challenges :  
# 
# ### writer : Faranak Alikhah 1954128

# ### 7. Validating phone numbers:

# In[ ]:


N=input()
for i in range(int(N)):
    A=input()
    if len(A)==10 and (A.isnumeric()):
        if (A[0]=='7' or A[0]=='8' or A[0]=='9' ):
            print('YES')
        else:
            print("NO")
    else:
        print("NO") 


# 
