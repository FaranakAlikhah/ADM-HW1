#!/usr/bin/env python
# coding: utf-8

# # Exercise 2.  :  
# ### writer : Faranak Alikhah 1954128

# ### 4.Recursive Digit Sum :

# In[ ]:


import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    #s=0
    while int(n)>=10:
            s=sum(int(i) for i in str(n))
            n=s
    x=n*k
    #a=0
    while x>=10:
        for i in str(x):
            a=sum(int(i) for i in str(x))
            x=a

    return(x)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()


# 

# 
