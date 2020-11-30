#mymodule.py
l=[1,2,3,4,5]
import mymodule
print(mymodule.l)

[1, 2, 3, 4, 5]

mymodule.l[0]=0
print(mymodule.l)

[0, 2, 3, 4, 5]
2.pandas package
import pandas as pd
pd.Series([2,4,6,8,10])
0     2
1     4
2     6
3     8
4    10
dtype: int64

3.Import a module that picks random number and write a program to fetch a random number from 1 to 100 on every run

import random
print(random.randint(1,100))
34

4.Import sys package and find the python path
import sys
print(sys.path)
['', '/env/python', '/usr/lib/python36.zip', '/usr/lib/python3.6', '/usr/lib/python3.6/lib-dynload', '/usr/local/lib/python3.6/dist-packages', '/usr/lib/python3/dist-packages', '/usr/local/lib/python3.6/dist-packages/IPython/extensions', '/root/.ipython']

5.Try to install a package and uninstall a package using pip
In [11]:
pip install pandas
Collecting pandas
  Downloading https://files.pythonhosted.org/packages/4d/51/bafcff417cd857bc6684336320863b5e5af280530213ef8f534b6042cfe6/pandas-1.1.4-cp36-cp36m-manylinux1_x86_64.whl (9.5MB)
     |████████████████████████████████| 9.5MB 5.0MB/s 
Requirement already satisfied: python-dateutil>=2.7.3 in /usr/local/lib/python3.6/dist-packages (from pandas) (2.8.1)
Requirement already satisfied: pytz>=2017.2 in /usr/local/lib/python3.6/dist-packages (from pandas) (2018.9)
Requirement already satisfied: numpy>=1.15.4 in /usr/local/lib/python3.6/dist-packages (from pandas) (1.18.5)
Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.6/dist-packages (from python-dateutil>=2.7.3->pandas) (1.15.0)
Installing collected packages: pandas
Successfully installed pandas-1.1.4
In [12]:
pip uninstall pandas
Uninstalling pandas-1.1.4:
  Would remove:
    /usr/local/lib/python3.6/dist-packages/pandas-1.1.4.dist-info/*
    /usr/local/lib/python3.6/dist-packages/pandas/*
Proceed (y/n)? y
  Successfully uninstalled pandas-1.1.4
