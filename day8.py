
1 List down all the error types and check all the errors using a py-thon program for all errors

#ZeroDivision error
a=6
b=a/0
print(b)
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-1-dceaed06f45a> in <module>()
      1 #ZeroDivision errror
      2 a=6
----> 3 b=a/0
      4 print(b)

ZeroDivisionError: division by zero

#intendation Error
s="KANYA"
for i in s:
print(i)
  File "<ipython-input-28-436bca5ffaff>", line 3
    print(i)
        ^
IndentationError: expected an indented block
#NameError
print(y)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-2-1d6447874c64> in <module>()
      1 #NameError
----> 2 print(y)

NameError: name 'y' is not defined
#Type Error
print('x' + 5)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-5-991421fd4f34> in <module>()
      1 #Type Error
----> 2 print('x' + 5)

TypeError: must be str, not int
#Index Error
l=[1,2,3,4,5]
print(l[10])
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-7-9f948310c65f> in <module>()
      1 #Index Error
      2 l=[1,2,3,4,5]
----> 3 print(l[10])

IndexError: list index out of range
#Iteration Error
s=iter([1,2,3])
next(s)
next(s)
next(s)
next(s)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-8-1530f087ad20> in <module>()
      4 next(s)
      5 next(s)
----> 6 next(s)

StopIteration: 
#Module not found error
import mymodule
print(mymodule.l)
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
<ipython-input-9-8c0d502b0fb1> in <module>()
      1 #Module not found error
----> 2 import mymodule
      3 print(mymodule.l)

ModuleNotFoundError: No module named 'mymodule'

---------------------------------------------------------------------------
NOTE: If your import is failing due to a missing package, you can
manually install dependencies using either !pip or !apt.

To view examples of installing some common dependencies, click the
"Open Examples" button below.
---------------------------------------------------------------------------
#Key error
dct = {1:2,2:4,5:7}
print(dct[9])
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-11-8b7515fb1e44> in <module>()
      1 #Key error
      2 dct = {1:2,2:4,5:7}
----> 3 print(dct[9])

KeyError: 9
#import error
from math import cuboid
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)
<ipython-input-12-d8873c08c90d> in <module>()
      1 #import error
----> 2 from math import cuboid

ImportError: cannot import name 'cuboid'

---------------------------------------------------------------------------
NOTE: If your import is failing due to a missing package, you can
manually install dependencies using either !pip or !apt.

To view examples of installing some common dependencies, click the
"Open Examples" button below.
---------------------------------------------------------------------------
#Value  Error
number=int(input("enter a number : "))
print(number)
enter a number : d
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-30-a57c7aab8802> in <module>()
      1 #Value  Error
----> 2 number=int(input("enter a number : "))
      3 print(number)

ValueError: invalid literal for int() with base 10: 'd'
2 Design a simple calculator app with try and except for all use cases
def add(a,b):
  try:
    print(a+z)
  except NameError:
    print("Please define the variable") #Nameerror
def sub(a,b): 
    try:
        print (a-b)
    except TypeError:
        print('please check the type of arguments')   
def mul(a,b):
  try:
    print(a+z)
  except:
    print("Please define the variable") 
def div(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print('cant divide by zero')        
op=int(input("enter operation\n 1.add\n 2.sub\n 3.mul\n 4.div\n"))
if op==1:
    print(add(2,4))
elif op==2:
    print( sub(5,'6'))
elif op==3:
    print(mul(3,s))
elif op==4:
     print( div(9,0))
else:
    print(op,"is not valid input")
    OUTPUT:
enter operation
 1.add
 2.sub
 3.mul
 4.div
3
Please define the variable
None
3 print one message if the try block raises a NameError and another for other errors
try:
  print(kee)
except NameError:
  print("Name error")
except:
  print("error")
  OUTPUT:
Name error
4) When try-except scenario is not required?

some exception can be handled by python itself ,

I such cases try-except scenario is not required

5 Try getting an input inside the try catch block

try:
  number1 = int(input())
except:
  print("Some error")
else:
  print("No error")
  OUTPUT:
No error
