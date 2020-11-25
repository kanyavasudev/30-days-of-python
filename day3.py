Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("program to merge two dict")
program to merge two dict
>>> fruits={'apples':100,'oranges':50}
>>> vegetables={'carrot':25,'tomato':40}
>>> print(fruits)
{'apples': 100, 'oranges': 50}
>>> print(vegetables)
{'carrot': 25, 'tomato': 40}
>>> vegetables.update(friuts)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    vegetables.update(friuts)
NameError: name 'friuts' is not defined
>>> vegetables.update(fruits)
>>> print(vegetables)
{'carrot': 25, 'tomato': 40, 'apples': 100, 'oranges': 50}
>>> print("program to remove a key from dictionary")
program to remove a key from dictionary
>>> vegetables.pop('tomato')
40
>>> print(vegetables)
{'carrot': 25, 'apples': 100, 'oranges': 50}
>>> print("program to map two lists into a dictionary")
program to map two lists into a dictionary
>>> d1={'sky','tree','lemon'}
>>> d2={'blue','green','yellow'}
>>> print(dict(zip(d1,d2)))
{'lemon': 'yellow', 'tree': 'green', 'sky': 'blue'}
>>> print("program to merge two dict")
program to merge two dict
>>> print("program to find the length of set")
program to find the length of set
>>> colours={'pink','red','blue','orange','green','violet'}
>>> print(len(colours))
6
>>> print("program to remove the intersection of a 2nd set from 1st set")
program to remove the intersection of a 2nd set from 1st set
>>> set1={1,2,3,4,5,6}
>>> set2={3,5,7,9,11}
>>> print(set1.intersection(set2))
{3, 5}
>>> 