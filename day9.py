
1) Create a lambda function that multiplies argument x with argument y


mul = lambda x,y : x*y
print(mul(2,3))
OUTPUT:
6
2 Write a Python program to create Fibonacci series to n using Lambda

def fibonacci(count):
    s = [0, 1]

    any(map(lambda _: s.append(sum(s[-2:])), range(2, count)))

    return s[:count]

print(fibonacci(int(input())))
3
OUTPUT:
[0, 1, 1]
3) Write a Python program that multiply each number of given list with a given number

lst = [1,2,3,4]
n=int(input("Enter the number : "))
lst2 = list(map(lambda x:x*n,lst))
print("List after multiplying with given number", lst2)
OUTPUT:
Enter the number : 3
List after multiplying with given number [3, 6, 9, 12]

4) Write a Python program to find numbers divisible by 9 from a list of numbers

l = [1,9,18,27,24,67,90]
mul = list(filter(lambda x:(x%9 == 0),l))
print("The numbers divisible by 9 : ",mul)
OUTPUT:
The numbers divisible by 9 :  [9, 18, 27, 90]
5) Write a Python program to count the even numbers in a given list of integers

l = [1,2,3,4,5,6,7,8,9]
even = list(filter(lambda x:(x%2 == 0),l))
print("The count of even numbers in a given list : ",len(even))
OUTPUT:
The count of even numbers in a given list :  4
