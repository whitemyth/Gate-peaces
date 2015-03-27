# !usr/bin/python3
# menudb.py
# a menu to drive the "codes" database

import sqlite3
# from lib.gate import ClientDatabase
from example.cdbt import ClientDatabase

db = sqlite3.connect("accessCodes.db")  #  database name
cursor = db.cursor()


ans=True
while ans:
    print ("""
    1.Add a Client
    2.Delete a Client
    3.Edit a client
    4.Edit Client code
    5.Client Report
    6.Exit/Quit
    """)
    client = ClientDatabase()
    ans = input("What would you like to do? ")
    if ans == "1":
        name = input("please enter client name")
        code = input("please enter client code")
        restriction = input("please enter client restriction")
        client.add(name, code, restriction)
        print("\n Client Added")

    elif ans == "2":
        name = input("Enter name of client to be deleted")
        client.delete(name)

    elif ans == "3":
        name = input("Please enter the name of the client you would like to edit")
        new_name = input("please enter the new name for this client")
        new_code = input("please enter the new code for this client")
        new_restriction = input("please enter the new restriction level for this client")
        client.edit(name, new_name, new_code, new_restriction)

    elif ans == "4":
        name = input("please enter the name of the client who's code you would like to change")
        new_code = input("please enter new code")
        client.change_code(name, new_code)

#This section should ask which client you'd like to edit (or possibly which criteria you'd like to
#search by to edit a client.  it should then ask you to change the information and then confirm before updating.

    elif ans == "5":
        user_list = client.list()
        for row in user_list:
            print("name: " + row[0])
            print("code: " + str(row[1]))
            print("restriction: " + row[2] + "\n")
            print("\n All Clients")

    elif ans=="6":
      print("\n Goodbye")
      ans =""
    else:
      print("\n Not Valid Choice Try again")