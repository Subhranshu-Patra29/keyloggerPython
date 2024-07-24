# --------------------------------------------------------------------------------------------------------
#                                         IMPORTING LIBRARIES

import mysql.connector
import connectMysql as conn

# --------------------------------------------------------------------------------------------------------
#                                         GLOBAL VARIABLES

mydb = conn.connect_to_mysql()
mycursor = mydb.cursor()

# --------------------------------------------------------------------------------------------------------

# Convert images or files data to binary format
def convert_data(filename):
    with open(filename, 'rb') as file:
        binary_data = file.read()
    return binary_data


def uploadSS(filename):
    global mydb, mycursor
    try:
        # INSERTION QUERY 
        query = """INSERT INTO SCREENSHOT(IMAGE) VALUES (%s)"""
        image = convert_data(filename)
        result = mycursor.execute(query, (image,))
        mydb.commit()
    except mysql.connector.Error as error:
        with open("log.txt", "a") as f:
            f.write("\n\nCould not upload file to MySQL server due to {error}\n\n")
    finally:
        if mycursor:
            mycursor.close()
            # print("Cursor closed.")
        if mydb.is_connected():
            mydb.close()
            # print("Database connection closed.")
            

uploadSS("owl.jpeg")