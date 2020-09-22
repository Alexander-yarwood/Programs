# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#"""
x = [1,3,4,5,7,2]

y = [4,5,6,7]

z = x + y  #makes a longer list out of x list and y list

y.extend(x) #puts the list of x onto the end of y

x[1] = 5 #changes position 1 (3 on the list) to 5

y.append(8) # adds 8 to the list y

x[1:4] #position 1 2 3
x[2:6] #position 2 3 4 5
x[2:]  #position 2 to end
x[:4]  #all up to, not including, 4

s = list(range(0,100))
print(s[10:40:3]) #lists 10 to 40 with a step of three

     
for t in["aberystwyth","bangor","cardiff","swansea"]:
    print(t + str(len(t)))  #prints the list with word length
    
         
u = "2,3,5,y,n,large"
v = u.split(",")  #makes a list with each list item ending at ","
print(v)

w = "hello and welcome to python"
h = w.split()   #makes a list, cutting at whitespace, like spaces and new lines
print(h)

i = ",".join(h) #makes a new string with "," as the seperator
print(i)
j = "".join(h) #joins the list with no seperation
print(j)
    
print(x)
print(y)
print(z)
#"""

userinp = input()  #user input
a = userinp.split() #splitting user input at spaces
print(len(a)) #printing number of words
print(userinp)  #printing what was typed

c = ""

for b in a:    #prints longest word
    if len(b) > len(c):  #compares the two lengths
        c = b       #makes c the longer word
        
print(c)