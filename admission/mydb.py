import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='shlok1005'

)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE db")

print("db created")