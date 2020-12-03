add an item to a list
seasons=["summer","winter","spring","fall"]
seasons.append("rainy")
print(seasons)
['summer', 'winter', 'spring', 'fall', 'rainy']
delete a item from a list
l1=[11,22,55,"peter",66,"james","ray"]
del l1[3]
print(l1)
[11, 22, 55, 66, 'james', 'ray']
del l1[3:5]
print(l1)
[11, 22, 55, 'ray']
l1.pop()
'ray'
print(l1)
[11, 22, 55]
l1.pop(0)
11
print(l1)
[22, 55]
l1.remove(22)
print(l1)
[55]
store largest number from list to a variable
l2=[153,189,100,44,569,2,0,4,89,65,24,23,27,15,147,5]
large=max(l2)
print(large)
569
print("store smallest number from list to a variable")
small=min(l2)
print(small)
0
l2.sort()
print(l2)
[0, 2, 4, 5, 15, 23, 24, 27, 44, 65, 89, 100, 147, 153, 189, 569]
to create a tuple and print reverse of the created tuple
tuple1=(25,86.3,"harry","lizzi",52,62.1,44,7.56)
rev=tuple(reversed(tuple1))
print(rev)
(7.56, 44, 62.1, 52, 'lizzi', 'harry', 86.3, 25)
to create a tuple and convert into a list
tuple2=(5,1,2,8,"ten",44,"nine")
print(tuple2)
(5, 1, 2, 8, 'ten', 44, 'nine')
list(tuple2)
[5, 1, 2, 8, 'ten', 44, 'nine']
