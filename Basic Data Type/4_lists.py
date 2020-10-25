#!/usr/bin/env python
# coding: utf-8

# # *section 2: Basic Data Type*
# 
# ### writer : Faranak Alikhah 1954128

# ### 4. Lists :
# 

# In[ ]:


if __name__ == '__main__':
    N = int(input())
    my_list=[]
    for i in range(N):
        A=input().split();
        
        if A[0]=="sort":
            my_list.sort();

        elif A[0]=="insert":
            my_list.insert(int(A[1]),int(A[2]))

        elif A[0]=="remove":
            my_list.remove(int(A[1]))
        
        elif A[0]=="append":
            my_list.append(int(A[1]))
        elif A[0]=="pop":
            my_list.pop()
        elif A[0]=="reverse":
            my_list.reverse()
        elif A[0]=="print":
            print(my_list)


# 
