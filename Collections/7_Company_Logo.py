#!/usr/bin/env python
# coding: utf-8

# # section 5: Colloctions  
# 
# ### writer : Faranak Alikhah 1954128

# ### 7.Company Logo :
# 
# 

# In[ ]:


import math
import os
import random
import re
import sys
from collections import Counter

if __name__ == '__main__':
    s =sorted(input())
    rep=Counter(s).most_common(3)
for i in rep:
    print(*i)


# 
