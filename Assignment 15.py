#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Please write a program using generator to print the numbers which can be divisible by 5 and 7
#between 0 and n in comma separated form while n is input by console.

def NumGen(n):
    # iterate from 0 to N
    for j in range(1, n + 1):

        # Short-circuit operator is used
        if j % 5 == 0 and j % 7 == 0:
            yield j

# Driver code
if __name__ == "__main__":

    # input goes here
    N = int(input("Enter values "))

    # Iterating over generator function
    for j in NumGen(N):
        print(j, end=" ")


# In[5]:


#Please write a program using generator to print the even numbers between 0 and n in comma separated form
#while n is input by console.

def NumGen(n):
    # iterate from 0 to N
    for j in range(0, n + 1):

        # Short-circuit operator is used
        if j % 2 == 0 :
            yield j

# Driver code
if __name__ == "__main__":

    # input goes here
    N = int(input("Enter values "))

    # Iterating over generator function
    for j in NumGen(N):
        print(j, end=" ")


# In[8]:


#Please write a program using list comprehension to print the Fibonacci Sequence in comma 
#separated form with a given n input by console.
n = int(input())
fib = [0, 1]
[fib.append(sum(fib[-2:])) for x in range(n)]
print(*(fib[:n]))


# In[ ]:


#Assuming that we have some email addresses in the "username@companyname.com" format,
#please write program to print the user name of a given email address. 
#Both user names and company names are composed of letters only.
import re
emailAddress = r"enter the name"
pat2 = "(\w+)@(\w+)\.(com)"
r2 = re.match(pat2,emailAddress)
print(r2.group(1))


# In[19]:


# a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. 
#Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
class Shape():
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self,length = 0):
        Shape.__init__(self)
        self.length = length

    def area(self):
        return self.length*self.length

Asqr = Square(5)
print(Asqr.area())      # prints 25 as given argument

print(Square().area())  # prints zero as default area


# In[ ]:




