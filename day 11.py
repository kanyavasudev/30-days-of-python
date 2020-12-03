1.program using zip()function and list function,create a merged list of tuples from
the two lists given..
list1=[1,2,'kanya',3]
list2=[2,3,'ram',4]
list3=[3,4,'raji',5]
list=list(zip(list1,list2,list3))
print(list)
OUTPUT:
[(1, 2, 3), (2, 3, 4), ('kanya', 'ram', 'raji'), (3, 4, 5)]
2.first create a range from 1to8.then using zip,merge the given list and range together
to creatr a new list of tuples

list1=["computer","maths","social","grammer","english","biology","language","zoology"]
rng1=list(range(1,8))
list=list(zip(list1,rng1))
print(list)

OUTPUT:
[('computer', 1), ('maths', 2), ('social', 3), ('grammer', 4), ('english', 5), ('biology', 6), ('language', 7)]
3.using sorted print the list in ascending order
numbers=[5,2,4,8,1,6]
sorted=sorted(numbers)
print(sorted)
OUTPUT:
[1, 2, 4, 5, 6, 8]

4.Filter even numbers using filter function

numbers=[44,2,5,88,56,55,54,51,23,27,9,8,3,6,5,7,4,22,11,13]
x=lambda m:m%2!=0
odd=list(filter(x,numbers))
print(odd)

OUTPUT:
[5, 55, 51, 23, 27, 9, 3, 5, 7, 11, 13]
