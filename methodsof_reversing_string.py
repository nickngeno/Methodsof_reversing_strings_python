#!/usr/bin/env python
# coding: utf-8

# In[86]:


# using for loop to reverse a string
user_input=input("enter your string here:")
x=""
if True:
    for i in user_input:
        x=i + x
    y.append(x)

if x==user_input:
    print("The string is palidrome")
else:
    print("The string is not palindrome")
    
    


# In[58]:


# using slicing to reverse a string
user_input=input("enter your string here:")
x=user_input[::-1]
if True:
    print ("The reverse of string",user_input.upper(),"is:\n" ,x.upper())


# In[63]:


# reversing string using while loop
user_input=input("Please input your string here:")
s=""
length_s=len(user_input)-1 #reads the strig from behind
while length_s >= 0:
    s=s + user_input[length_s] 
    length_s=length_s -1
    
print(s)


# In[64]:


# using join() to reverse string
user_input=input("Please input your string here:")
s=""
s="".join(reversed(user_input))
print(s)


# In[84]:


# using list reverse to reverse a string
user_input=input("Please input your string here:")
s=""
s=list(user_input)
print("".join(reversed(s)))
# return (s)


# In[110]:


# using recursion to reverse a string
def reverse_recursion(s):
    if len(s)==0:
        return s
    else:
        return reverse_recursion(s[1:])+s[0]
reverse_recursion("kim")


# In[ ]:




