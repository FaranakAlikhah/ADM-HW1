#!/usr/bin/env python
# coding: utf-8

# # Exercise 2. Birthday Cake :  
# ### writer : Faranak Alikhah 1954128

# ### 1. birthday cake  :

# In[ ]:


import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # THROUGH THIS FUNCTION WE CAN FIND THE MAX AND COUNT THE NUMBER OF REPETITIONA
    maximum=0
    candel_count=0
    for i in range(len(candles)):
        if candles[i]>maximum:
            maximum=candles[i]
            candel_count=1
        elif candles[i]==maximum:
            candel_count+=1
    return(candel_count)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()


# 

# 
