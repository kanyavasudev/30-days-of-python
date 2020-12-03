
Write a Python program for all the cases which can check a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).

import re
string = input()
pattern = re.compile("[A-Za-z0-9]+")
if pattern.fullmatch(string):
  print("True")
else:
  print("False")
OUTPUT:
34rtEd
True
Write a Python program that matches a word containing 'ab'.

pattern = 'ab'
text = input()
if re.search(pattern,text):
    print('match found')
else:
    print('not found')
OUTPUT:
radtabhujab
match found

Write a Python program to check for a number at the end of a word/sentence.
string = input()
r=re.compile(r".*[0-9]$")
if r.match(string):
  print("True")
else:
  print("False")
OUTPUT:
sedfr667
True
Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string


pattern=r"([0-9]{1,3})"
t = "4,21,and 567 are important questions"
s = re.finditer(pattern,t)
print("Numbers with length 1 to 3 in the string : ")
for n in s:
  print(n.group(0))
OUTPUT:
Numbers with length 1 to 3 in the string : 
4
21
567
Write a Python program to match a string that contains only uppercase letters

import re
reg = r'^[A-Z]*$'
s = input()
if re.search(reg,s): 
  print('String contains only uppercase letters')
else:
  print('String does not contains only uppercase letters')
OUTPUT:
ADT
String contains only uppercase letters
