# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""
number = input()
secnum = input()
print(int(number)*(int(secnum)))    #get two numbers from user and 
                                    #multiply the int values
"""

stock = {
    "apple": 10,
    "strawberry": 35,
    "orange": 9,
    "beetroot": 20,
    "carrot": 13
}

price = {
    "apple": 1.4,
    "strawberry": 2.0,
    "orange": 1.0,
    "beetroot": 2.5,
    "carrot": 1.2
}

cymraeg = {
    "apple": "afal",
    "strawberry": "mefus",
    "orange": "oren",
    "beetroot": "betys",
    "carrot": "moron"
}

customer1 = ["apple", "orange", "apple", "beetroot", "beetroot"]


""""
j = 0
for i in price.keys():
    j = j + (price[i] * stock[i])
    
print(j)        #calculate the total value of all stock
"""

"""
l = 0
for k in customer1:
    l = l + price[k]
    stock[k] = stock[k] - 1
    
print("The bill is " + str(l))
print(stock)                    #take the order, remove the stock,
                                #calculate the price
"""
print("enter new smoothie english")
english = input()

print("enter new smoothie Welsh")
welsh = input()

print("enter the stock amount")
stocknum = input()

print("enter the cost")
cost = input()


stock[english] = stocknum
cymraeg[english] = welsh
price[english] = cost
print(stock)

print(price)

print("english")
for m in stock:
    print(str(m) + " costs £" + str(price[m]))
    print()
    
    
print("welsh")
for m in stock:
    print(str(cymraeg[m]) + " costs £" + str(price[m]))
    print()