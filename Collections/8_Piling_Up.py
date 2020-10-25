#!/usr/bin/env python
# coding: utf-8

# # section 5: Colloctions  
# 
# ### writer : Faranak Alikhah 1954128

# ### 8.Piling Up :
# 
# 

# In[ ]:


from collections import deque
from  math import inf 
num_test=int(input())
 
for i in range(num_test):
    flag=True
    num_cube=int(input())
    cubeLength=deque(map(int,input().split()))
    current_cube=inf

    while len(cubeLength)>0 :
        l_cube=cubeLength[0]
        r_cube=cubeLength[-1]
        if l_cube>=r_cube and l_cube<=current_cube:
            cubeLength.popleft()
            current_cube=l_cube
        elif l_cube<r_cube and r_cube<=current_cube:
            cubeLength.pop()
            current_cube=r_cube
        else :
            flag=False
            break
    if flag==True:
        print("Yes")
    else:
        print("No")


# 
