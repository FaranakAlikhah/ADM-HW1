#!/usr/bin/env python
# coding: utf-8

# # Exercise 3. Viral Advertising  :  
# ### writer : Faranak Alikhah 1954128

# 

# In[ ]:


import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    comulative=0
    population=5
    for i in range(int(n)):
       
            like=population//2
            comulative+=like
            population=like*3

    
    
    return(comulative)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()


# 

# 
