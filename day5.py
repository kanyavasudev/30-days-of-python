1.create function getting two integer input from user & print the folowing
Addition
Subtraction
Multiplicatton
Division

def funt(a,b):
	print("addition of two numbers is:",a+b)
	print("subtraction of two numbers is:",a-b)
	print("multiplication of two numbers is:",a*b)
	print("division of two numbers is:",a/b)
a=int(input("enter number 1:"))
b=int(input("enter number 2:"))
funt(a,b)
OUTPUT:
enter number 1:5
enter number 2:2
addition of two numbers is: 7
subtraction of two numbers is: 3
multiplication of two numbers is: 10
division of two numbers is: 2.5

2.Create a function called covid and& it shout accept patient name and body temperature
by default the temperature is 98degree

def covid(name,temp=98):
    print("patient name:",name)
    print("body temperature:",temp)
covid("kanya",100)
covid("ahana")
OUTPUT:
patient name: kanya
body temperature: 100
patient name: ahana
body temperature: 98
