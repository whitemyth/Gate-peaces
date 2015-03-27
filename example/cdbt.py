# usr/bin/python3
# cbdt.py
# test file to test the ClientDatabase class
import sqlite3


class ClientDatabase:
    def __init__(self):
        self.db = sqlite3.connect("accessCodes.db")

    def add(self, name, code, restriction):
        self.db.execute('''INSERT INTO codes (client_name, client_code, client_restrictions)
            VALUES(?,?,?)''', (name, code, restriction))
        self.db.commit()

    def delete(self, name):
        self.db.execute('''DELETE FROM codes WHERE client_name=?''', (name,))
        self.db.commit()
        print("Records Deleted ", self.db.total_changes)

    def edit (self, name, new_name, new_code, new_restriction):
        self.db.execute('''UPDATE codes SET client_name=?, client_code=?, client_restrictions=? WHERE client_name=?''', (new_name, new_code, new_restriction, name))
        self.db.commit()
        print("client updated")

    def change_code(self, name, new_code):
        self.db.execute('''UPDATE codes SET client_code=? WHERE client_name=?''', (new_code, name))
        self.db.commit()
        print("code updated")

    def list(self):
        cursor = self.db.execute('''SELECT client_name, client_code, client_restrictions FROM codes''')
        return cursor.fetchall()


# instantiate the class ClientDatabase, create an object of ClientDatabase, the object is called "client"
# client = ClientDatabase()
# client.add("Alex", 1234, "Staff")
# client.delete("Alex")
# client.edit("Alex", "Alex2", 4321, "Nobody")
# user_list = client.list()
# for row in user_list:
#     print("name: " + row[0])
#     print("code: " + row[1])
#     print("restriction: " + row[2] + "\n")


