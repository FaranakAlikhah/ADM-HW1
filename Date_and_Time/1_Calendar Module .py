#!/usr/bin/env python
# coding: utf-8

# # section 6: Date and Time :  
# 
# ### writer : Faranak Alikhah 1954128

# ### 1.Calendar Module :
# 
# 

# In[ ]:


import calendar 
T=input().split()
m=int(T[0])
d=int(T[1])
y=int(T[2])
# m,d,y=map(int,input().split())
days_name=['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
case=calendar.weekday(y,m,d)
print(days_name[case])


# 
