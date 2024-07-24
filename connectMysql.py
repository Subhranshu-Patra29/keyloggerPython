# --------------------------------------------------------------------------------------------------------
#                                         IMPORTING LIBRARIES

import mysql.connector as connection

# --------------------------------------------------------------------------------------------------------

def connect_to_mysql():
    mydb = None
    mycursor = None
    try:
        mydb = connection.connect(host = "localhost", user = "root", passwd = "dhanna", database = "keylogger")
        mycursor = mydb.cursor()
        print("Connection Succesfull !!!")
        return mydb
    except Exception as e:
        print("Database connection failure.")
        print(format(e))
    # finally:
    #     if mydb.is_connected():
    #         mycursor.close()
    #         mydb.close()
    #         print("Connection closed.")
    
connect_to_mysql()