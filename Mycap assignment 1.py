#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Filename = input("Input the file name ")
f_extns = Filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))
x= ".py"
y= ".java"
z= ".c"
a= ".CPP"
if x in Filename:
    print("Python")
elif y in Filename:
        print("Java")
elif z in Filename:
        print("C")    
elif a in Filename:
        print("C++")
    


# In[ ]:


import math
radius = float(input("Radius of the circle is "))
area = math.pi*radius*radius
print(area)

