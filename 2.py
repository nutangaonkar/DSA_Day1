#1.simple IF


"""#WAP to accept any on number and check pos, neg and zeo
num = int(input("enter any one number:"))
if num > 0:
    print(" positive number")
if num < 0:
    print(" negative number")
if num == 0:
    print("number is zero")        
"""

"""
# Greater number among 5 numbers
a = int(input("enter number1: "))
b = int(input("enter number2: "))
c = int(input("enter number3: "))
d = int(input("enter number4: "))
e = int(input("enter number5: "))
if a > b and a> c and a>d and a>e:
    print("a is greater", a)
if b > a and b> c and b>d and b>e:
    print("b is greater", b)
if c > b and c> a and c>d and c>e:
    print("c is greater", c) 
if d > a and d > b and d > c and d > e:
    print("d is greater", d) 
if e > a and e > b and e > c and e > d:
    print("e is greater", e)              
"""


#2.If-else

"""username = input("enter username: ")
password = input("Enter password: ")
if username == password:
    print("login successful")
else:
    print("login failed")    
"""


"""
#WAp to accept phy, chem, maths marks calculate total and percentage and if percentage is greater than equal to 60 and gender is equal to male so he is eligible for placement else eligible for data entry job

p1 = int(input("Enter marks of p1: "))
p2 = int(input("Enter marks of p2: "))
p3 = int(input("Enter marks of p3: "))
gender = input("enter gender: ")
total = p1+p2+p3
percentage = total/3.0
print("percentage", percentage)
if percentage >= 60 and gender == "male":
    print("eligible for placement")
else:
    print("eligible for data entry job")    
"""    

#3.Nested if-else
"""        
#WAP to accept A,B,C and find max value

a = int(input("Enter marks of a: "))
b = int(input("Enter marks of b: "))
c = int(input("Enter marks of c: "))

if a > b:
    if a>c:
        print("a is greater")
    else:
        print("c is greater")
else:
    if b > c:
        print("b is greater")
    else:
        print("c is greater") 
"""

"""
day = input("enter day {sunday-saturday}:")
if day== "sunday" or day== "Sunday" or day== "saturday" or day== "saturday":
    print("its weekend")
else:
    print("working day")
"""


"""
#WAP to check wheter entered character is letter, digit or special character
x = ord(input("enter here: "))

if x >= 65 and x <= 90: #A-Z
    print(" upper case character")
elif x >= 97 and x <= 122: #a-z
    print(" lowercase")    
elif x >= 48 and x <=57: #0-9
    print("its digit") 
else:
    print("special character")   """ 


"""
#WAP for change calculations w.r.t. total amount
amount = int(input("enter amount: "))
print(" 100 note= ", amount//100)
print(" 50 note= ", (amount % 100)//50)
print(" 20 note= ", ((amount % 100) % 50)//20)
print("10 notes= ", (((amount % 100)% 50)%20)//10)
print("5 notes= ", ((((amount % 100)% 50)%20)%10)//5)

"""
