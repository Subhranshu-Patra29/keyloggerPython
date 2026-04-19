# --------------------------------------------------------------------------------------------------------
#                                         IMPORTING LIBRARIES

import mysql.connector as connection

# --------------------------------------------------------------------------------------------------------

def uploadSystemDetails(mydb, file):
    mycursor = mydb.cursor()
    try:
        # INSERTION QUERY 
        query = "INSERT INTO SYSTEM_INFO(Parameter, Value) VALUES (%s, %s)"
        for key, value in file.items():
            mycursor.execute(query, (key, value))
        mydb.commit()
    except connection.Error as error:
        print(error)
        with open("log.txt", "a") as f:
            f.write("\n\nCould not upload system information to MySQL server. \n\n")  