
Create a JSON of all object types and import the JSON into a SQL Database Note: The JSON file should have valus of all Datatypes
example.json
[

[

    {"name":"kanya", "age":20,"city":"chennai"},
    [1,2,3],
    [3,2,1],
    "Myself",
    35,
    35.5,
    true,
    null]
]
import sqlite3
import json
In [ ]:
con = sqlite3.connect("test.db")
print("Database Opened")
Database Opened
In [ ]:
cursor = con.cursor()
try:
    cursor.execute("CREATE TABLE MINE"
                   "("
                   + "dictinary BLOB,"
                   + "list BLOB,"
                   + "tuple BLOB,"
                   + "string varchar(50),"
                   + "Integer INTEGER,"
                   + "flo FLOAT,"
                   + "Bool BOOLEAN,"
                   + "None BLOB"
                     ");")
except Exception as e:
    print("Error :", e)
else:
    print("Table created")
output:
Table created

datafile = open("example.json")
dataset = json.load(datafile)
dataframe = []
for row in dataset:
    data = (str(row[0]), str(row[1]), str(row[2]), str(row[3]), int(row[4]),
            float(row[5]), bool(row[6]), row[7])
    dataframe.append(data)

try:
    cursor.executemany("INSERT INTO MINE VALUES (?,?,?,?,?,?,?,?)", dataframe)
except Exception as e:
    print("Error : ", e)
else:
    con.commit()
    print("Data inserted")
OUTPUT
Data inserted

try:
    cursor.execute("SELECT * from MINE")
except Exception as e:
    print("Error : ", e)
else:
    for row in cursor.fetchall():
        print(row)
("{'name': 'Kanya', 'age': 20, 'city': 'chennai'}", '[1, 2, 3]', '[3, 2, 1]', 'Myself', 35, 35.5, 1, None)

con.close()
