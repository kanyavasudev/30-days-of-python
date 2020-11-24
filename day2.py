Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=b=c=10
>>> a/10
1.0
>>> b/50
0.2
>>> c/60
0.16666666666666666
>>> str=python
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    str=python
NameError: name 'python' is not defined
>>> str='python'
>>> str.replace('t','g',3)
'pyghon'
>>> a,b=20,5.2
>>> print(a,b)
20 5.2
>>> type(a)
<class 'int'>
>>> 
>>> int(b)
5
>>> float(a)
20.0
>>> print(a,b)
20 5.2
>>> print(float(a),int(b))
20.0 5
>>> 