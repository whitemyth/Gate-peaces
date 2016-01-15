#!usr/bin/python3
#accessDb.py
#sample data base for the users containing names, codes, times, and restrictions

import sqlite3

db = sqlite3.connect("accessCodes.db")  #  database name
cursor = db.cursor()

#cursor.execute('''
#    CREATE TABLE codes(id INTEGER PRIMARY KEY, client_name TEXT,
#                    client_code INTEGER,  client_restrictions TEXT)
#''')
#db.commit()

#add information

client_name1 = '?'
client_code1 = '?'
client_restricitons1 = '?'

cursor.execute('''INSERT INTO codes(client_name, client_code, client_restrictions)
                  VALUES(?,?,?)''', (client_name1, client_code1, client_restricitons1))

#print('First user inserted')






#display information

#display all

cursor.execute('''SELECT client_name, client_code, client_restrictions FROM codes''')
client_name1 = cursor.fetchall() #retrieve the first row use fetchall() for all data
print(client_name1) #Print the first column retrieved(user's name)
all_rows = cursor.fetchall()
for row in all_rows:
    print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))

db.commit()


#  Or  display all
cursor = db.execute('''SELECT client_name, client_code, client_restrictions FROM codes''')
for row in cursor:
   print ("client_name = ", row[0])
   print ("client_code = ", row[1])
   print ("client_restrictions = ", row[2], "\n")





#display_one
client_name1 = 'Sam Axe'

cursor.execute('''SELECT client_name, client_code, client_restrictions FROM codes WHERE client_name=?''', (client_name1,))
client_name1 = cursor.fetchone() #retrieve the first row use fetchall() for all data
print(client_name1) #Print the first column retrieved(user's name)

db.commit()


#remove information
db.execute("DELETE from codes where client_code= 1234;")
db.commit()

print ("Records Deleted ", db.total_changes)

cursor = db.execute("SELECT client_name, client_code, client_restrictions from codes")
for row in cursor:
   print ("client_name = ", row[0])
   print ("client_code = ", row[1])
   print ("client_restrictions = ", row[2], "\n")





#edit information

db.execute("UPDATE codes set client_code = 1224 where client_name= 'Sam Axe'")
db.commit
print ("Total number of rows updated :", db.total_changes)

cursor = conn.execute("SELECT client_name, client_code, client_restrictions  from codes")
for row in cursor:
   print ("client_name = ", row[0])
   print ("client_code = ", row[1])
   print ("client_restrictions = ", row[2], "\n")

print ("Operation done successfully")


db.close()
