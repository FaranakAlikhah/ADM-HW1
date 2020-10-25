#!/usr/bin/env python
# coding: utf-8

# # *section 2: Basic Data Type*
# 
# ### writer : Faranak Alikhah 1954128

# ### 3. Finding the percentage :
# 

# In[ ]:


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    result=list(student_marks[query_name])
    comulate=sum(result)
    result_per= comulate/len(result);
    print("%.2f" % result_per);


# 
