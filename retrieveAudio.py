# --------------------------------------------------------------------------------------------------------
#                                         IMPORTING LIBRARIES

import mysql.connector as connection
import connectMysql as conn

# --------------------------------------------------------------------------------------------------------

def retrieve_audio(mydb, start_file_id, end_file_id):
    try:
        query = "SELECT ADID, AUDIO_DATA FROM AUDIO WHERE ADID BETWEEN %s AND %s"
        cursor = mydb.cursor()
        cursor.execute(query, (start_file_id, end_file_id))
        rows = cursor.fetchall()

        for row in rows:
            audio_id, audio_data = row
            output_filename = f"retrieved_audio_{audio_id}.wav"

            # Write the binary data to a file
            with open(output_filename, "wb") as file:
                file.write(audio_data)
            print(f"Successfully retrieved and saved to {output_filename}")

    except connection.Error as error:
        print(error)
        with open("log.txt", "a") as f:
            f.write(f"\n\nCould not retrieve audio file from MySQL server. \n\n")
    finally:
        if cursor:
            cursor.close()

def main():
    mydb = conn.connect_to_mysql()
    if mydb is None:
        print("Failed to connect to the database.")
        return
    
    retrieve_audio(mydb, 1,6)

    if mydb.is_connected():
        mydb.close()
        print("Database connection closed.")

if __name__ == "__main__":
    main()