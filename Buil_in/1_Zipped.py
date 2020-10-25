#!/usr/bin/env python
# coding: utf-8

# # section 8: Built-Ins:  
# 
# ### writer : Faranak Alikhah 1954128

# ### 1.Zipped :
# 
# 

# In[ ]:


N,X=map(int,input().split())
sheet_marks=[]
for i in range(X):
    sheet_marks+=[map(float,input().split())]
    #sheet_marks.append(map(int,input().split()))
zipFile=zip(*sheet_marks)
for i in zipFile:
    print(sum(i)/len(i))


# 
