#!/usr/bin/env python
# coding: utf-8

# # section 6: Date and Time :  
# 
# ### writer : Faranak Alikhah 1954128

# ### 2.Time Delta :
# 
# 

# In[ ]:


import math
import os
import random
import re
import sys
import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    A =datetime.datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    F =datetime.datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    return (str(int(abs((A-F).total_seconds()))))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()


# 
