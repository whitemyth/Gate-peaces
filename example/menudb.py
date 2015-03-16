# !usr/bin/python3
# menudb.py
# a menu to drive the "codes" database

import sqlite3

db = sqlite3.connect("accessCodes.db")  #  database name
cursor = db.cursor()

ans=True
while ans:
    print ("""
    1.Add a Client
    2.Delete a Client
    3.Edit a client
    4.Client Report
    5.Exit/Quit
    """)
    ans=input("What would you like to do? ")
    if ans=="1":
        client_name1 = input("Please enter Client's full name" '?')
        client_code1 = input("please enter Client's access code" '?')
        client_restrictions1 = input("please enter Access Level\n Staff\n Boarder\n Service\n" '?')

        cursor.execute('''INSERT INTO codes(client_name, client_code, client_restrictions)
            VALUES(?,?,?)''', (client_name1, client_code1, client_restrictions1))
        db.commit()
        print("\n Client Added")

    elif ans=="2":
        client_name1 = input("Enter the full name of the client you'd like to remove" '?')
        db.execute('''DELETE from codes where client_name =?''', (client_name1,))
        db.commit()
        print ("Records Deleted ", db.total_changes)



    elif ans=="3":
      print("\n Client Record Updated")


#This section should ask which client you'd like to edit (or possibly which criteria you'd like to
#search by to edit a client.  it should then ask you to change the information and then confirm before updating.

    elif ans=="4":
      cursor = db.execute('''SELECT client_name, client_code, client_restrictions FROM codes''')
      for row in cursor:
        print ("client_name = ", row[0])
        print ("client_code = ", row[1])
        print ("client_restrictions = ", row[2], "\n")

      print("\n All Clients")

    elif ans=="5":
      print("\n Goodbye")
      ans =""
    else:
      print("\n Not Valid Choice Try again")