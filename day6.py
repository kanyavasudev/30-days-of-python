1.Loop through list of number and add +2
list=[]
n=int(input("Enter the number of elements :"))
print("Enter list elements")
for i in range(0,n):
    element=int(input())
    list.append(element)

print("list element :",list)
res=[ x+2 for x in list]
print("list after adding 2:",res)

OUTPUT:
Enter the number of elements :6
Enter list elements
8
5
3
6
9
5
list element : [8, 5, 3, 6, 9, 5]
list after adding 2: [10, 7, 5, 8, 11, 7]

2.TO get below pattern
54321
4321
321
21
1
n=5
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end="")

    print()
    
OUTPUT:
54321
4321
321
21
1

3.fibonacci series
n=int(input("Length of the seq"))
a=0
b=1
print("fibonacci seq")
while(a<n-1):
    print(a)
    print(b)
    a=a+b
    b=a+b
    
OUTPUT:
Length of the seq 3
fibonacci seq
0
1
1
2

4.ARMSTRONG NUMBER
num=int(input("enter a number"))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum=sum+(digit**3)
    temp//=10

if num==sum:
    print(num,"is armstrong number")
else:
    print(num,"is not armstrong number")
    
OUTPUT:
enter a number596
596 is not armstrong number

5.Multiplication table of 9
n=int(input("enter number :"))
for i in range(1,n+1):
    print("9 x "+str(i) +"=",i*9)

OUTPUT:
enter number :6
9 x 1= 9
9 x 2= 18
9 x 3= 27
9 x 4= 36
9 x 5= 45
9 x 6= 54

6.number is positive or negative
n=int(input("enter a number:"))
if (n>=0):
    print("positive")
else:
    print("negative")
        
OUTPUT:
enter a number:8
positive

7.convert number of days to ages
n=int(input(" enter no.of days"))
age=n//365
print("age is",age)

OUTPUT:
 enter no.of days5698
age is 15

8.Trignomentric funtions
import math
a=math.pi/6
b=9
c=2
print("The sine of pi/6:",math.sin(a))
print("The cos of pi/6:",math.cos(a))
print("The tan of pi/6:",math.tan(a))
print("The degree of pi/6:",math.degrees(a))

OUTPUT:
The sine of pi/6: 0.49999999999999994
The cos of pi/6: 0.8660254037844387
The tan of pi/6: 0.5773502691896257
The degree of pi/6: 29.999999999999996

9.Basic calci using if

    print("Calculator")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")
ch=int(input("Enter Choice(1-4): "))

if ch==1:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a+b
    print("Sum = ",c)
elif ch==2:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a-b
    print("Difference = ",c)
elif  ch==3:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a*b
    print("Product = ",c)
elif ch==4:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a/b
    print("Quotient = ",c)
else:
    print("Invalid Choice")

OUTPUT:
Calculator
1.Add
2.Substract
3.Multiply
4.Divide
Enter Choice(1-4): 2
Enter A:5
Enter B:2
Difference =  3
