import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Nanayaasql23',
)

cursorObject = database.cursor()

cursorObject.execute('CREATE DATABASE papaco')

print('Database "papaco" created successfully!')
