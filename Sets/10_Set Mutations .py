#!/usr/bin/env python
# coding: utf-8

# # *section 4: Strings*
# 
# ### writer : Faranak Alikhah 1954128

# ### 10.Set Mutations :
# 

# In[ ]:


number_elements=int(input())
main_st=set(map(int,input().split()))
num_comments=int(input())
for i in range(num_comments):
        comments,_=input().split()
        second_st=set(map(int,input().split()))
        if comments=='intersection_update':
            main_st.intersection_update(second_st)
        elif comments=='update':
            main_st.update(second_st)
        elif comments=='symmetric_difference_update':
            main_st.symmetric_difference_update(second_st)
        elif comments=='difference_update':
            main_st.difference_update(second_st)
    

print(sum(main_st)) 


# 
