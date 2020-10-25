#!/usr/bin/env python
# coding: utf-8

# # section 8: Built-Ins:  
# 
# ### writer : Faranak Alikhah 1954128

# ### 2.Athlete Sort :
# 
# 

# In[ ]:


import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    arr.sort(key=lambda x: x[k])
    #arr=sorted(arr ,key=itemgetter(k))
    for i in arr:
        print(*i)


# 
