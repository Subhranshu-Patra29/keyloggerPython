# --------------------------------------------------------------------------------------------------------
#                                         IMPORTING LIBRARIES

import mysql.connector as connection
import connectMysql as conn

# --------------------------------------------------------------------------------------------------------

# Convert images or files data to binary format
def convert_data(filename):
    with open(filename, 'rb') as file:
        binary_data = file.read()
    return binary_data

def uploadSS(mydb, filename):
    mycursor = mydb.cursor()
    try:
        # INSERTION QUERY 
        query = """INSERT INTO SCREENSHOT(Filename, IMAGE) VALUES (%s, %s)"""
        image = convert_data(filename)
        result = mycursor.execute(query, (filename, image))
        mydb.commit()
    except connection.Error as error:
        print(error)
        with open("log.txt", "a") as f:
            f.write("\n\nCould not upload file to MySQL server. \n\n")