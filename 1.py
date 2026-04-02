#Dynamically Typed
# math = 50
# name = "Nutan"
# pi = 3.142
# result = True

# type function - To check datatype
# print(type(name))
# print(type(result))

# id function - To check address
# math = 60 
# chem= 60
# phy = 60
# hindi = 71
# print(id(math))
# print(id(name))
# print(id(chem))
# print(id(math))
# print(id(phy))
# print(id(hindi))


# Add diagonal element
List = [[1,2,3],
       [4,5,6],
       [7,8,9]]

# Type Casting
#print(6+7)     
#print("3"+"5")

#val1 = input("Enter element1:") #3
#val2 = input("Enter element2:") #5
#print(val1+val2) #35

#val3 = int(input("Enter element 1:")) #5
#val4 = int(input("Enter element 2:")) #8
#print(val3 + val4) #13

"""
#int() used to convert to integer
print(int(3.14)) #3
print(int(True)) #1
print(int(False)) #2
(int("4.21"))  #Cannot convert string name to int
# we cannot convert complex value to int
# we cannot convert floating point value string to int
"""


"""
#float() used to convert to float
print(float(True)) #1.0
print(float(False)) #0.0
print(float(3))    #3.0
print(float(50+21)) #71.0
print(float("4")) #print(float("name"))
# we cannot convert complex value to float
#Cannot convert string name to int

"""

"""
#complex() used to convert
print(complex(3))
print(complex(12.5))
print(complex(True))
print(complex(False))
print(complex("5"))
print(complex("5.6"))
#print(complex("name"))
print(complex(5, -3))
print(complex(True,False))
"""

"""
#bool() is used to convert
print(bool(0)) #False
print(bool(0.0))  #False
print(bool(15))
print(bool(3.14))
print(bool(1+2j))
print(bool(0+0j))  #False
print(bool(-1))
print(bool(False))  #False
print(bool(True))
print(bool())  #False
"""

"""
#swapping of two interger using 3rd varibale
val1 = int(input("Enter value 1:"))
val2 = int(input("Enter value 2:"))
print("before swapping:",val1,val2)
temp = val1
val1 = val2
val2 = temp
print("After swapping:",val1,val2)
"""


"""
#swapping of two interger without using 3rd varibale
val1 = int(input("Enter value 1:"))
val2 = int(input("Enter value 2:"))
print("before swapping:",val1,val2)

val1 = val1+val2
val2 = val1-val2
val1 = val1-val2
print("After swapping:",val1,val2)
"""


"""
#Take marks of 3 subjects and calculate pecentage
p1 = int(input("Enter marks of p1: "))
p2 = int(input("Enter marks of p2: "))
p3 = int(input("Enter marks of p3: "))
total = p1+p2+p3
percentage = total/3.0
print("percentage=",percentage)
"""


"""
#Calculate simple interest
Principle_amount = float(input("enter loan amount:"))
rate = int(input("enter rate of interest:"))
time = int(input("enter the duration of loan amount:"))
simple_interest = (Principle_amount*rate*time)/100
print("simple_interest: ", simple_interest)
"""


"""
#WAP to height of user in feet and convert it into inch and centimeter
height = float(input("Enter height in feet: "))
inch = height*12
cm = inch * 2.54
print("Height in inch: ", inch)
print("height in cm: ", cm)
"""

"""
#Reverse a number
num = int(input("enter a number: ")) #123
a = num % 10 #3
num = num // 10 #12
b = num % 10 #2
c = num //10
rev = a*100+b*10+c*1
print("reverse number: ", rev)
"""

"""
num = int(input("enter a number: ")) #123456
a = num % 10 #6
num = num //10 #12345
b = num % 10 #5
num = num // 10 #1234
c = num % 10 #4
num = num // 10 #123
d = num % 10 #3
num = num // 10 #12
e = num % 10 #2
f = num //10 #1
rev = a*100000+b*10000+c*1000+d*100+e*10+f
print("reverse number: ", rev)
"""

"""
# Identity Operator
a = 10
b = 10 
print(a is b) #True
print(a is not b) #False

c = 20
d = 10 
print(c is d) #False
print(c is not d) #True
"""


"""
#Membership operator
name = "Nutan"
print("a" in name) #True
print("g" in name) #False
print("g" not in name) #True
"""

