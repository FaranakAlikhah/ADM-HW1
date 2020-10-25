#!/usr/bin/env python
# coding: utf-8

# # section 13.Regex and Parsing challenges :  
# 
# ### writer : Faranak Alikhah 1954128

# ### 10.HTML Parser - Part 2 :

# In[ ]:


from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, my_data):
        if '\n' not in my_data:
            print('>>> Single-line Comment')
            print(my_data)
        elif '\n' in my_data:
            print('>>> Multi-line Comment')
            print(my_data)
    def handle_data(self, my_data):
        if my_data != '\n':
            print('>>> Data')
            print(my_data)
  
  
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()


# 
