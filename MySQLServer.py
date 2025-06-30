import mysql.connector
from mysql.connector import errorcode

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="akhonatrom"
    )
    mycursor = mydb.cursor()

    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Failed to connect to MySQL server or create database: {err}")

finally:
    try:
        if mycursor:
            mycursor.close()
        if mydb:
            mydb.close()
    except NameError:
        pass