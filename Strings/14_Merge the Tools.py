#!/usr/bin/env python
# coding: utf-8

# # *section 3: Strings*
# 
# ### writer : Faranak Alikhah 1954128

# ### 14.Merge the Tools! :
# 

# In[ ]:


def merge_the_tools(string, k):
    # your code goes here
    sequ=[]
    counter=0
    delta=len(string)//k
    for i in range(delta):
        sequ.append(string[counter:counter+k])
        counter=counter+k
    for j in sequ:
        print( ''.join( list( dict.fromkeys( list( j)).keys() ) ) )


# 
