# --------------------------------------------------------------------------------------------------------
#                                         IMPORTING LIBRARIES

import mysql.connector as connection

# --------------------------------------------------------------------------------------------------------

def connect_to_mysql():
    mydb = None
    try:
        mydb = connection.connect(host = "localhost", user = "root", passwd = "dhanna", database = "keylogger")
        print("Connection Succesfull !!!")
        return mydb
    except Exception as e:
        print("Database connection failure.")
        print(format(e))
    
# connect_to_mysql()