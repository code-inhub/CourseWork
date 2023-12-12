import mysql.connector as sql

connection = sql.connect( 
    host="localhost",
    user="root",
    password = "*****",
    port = "3306")   

cursor = connection.cursor()
1
cursor.execute("CREATE DATABASE IF NOT EXISTS test_database")
cursor.execute("USE test_database")

cursor.execute('''
    CREATE TABLE IF NOT EXISTS test_table (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255)
    )
# ''')
cursor.execute("INSERT INTO test_table (name) VALUES ('Anshul')")
cursor.execute("INSERT INTO test_table (name) VALUES ('MADHAN')")
cursor.execute("INSERT INTO test_table (name) VALUES ('NOONE')")
cursor.execute("SELECT * FROM test_table")
for row in cursor:
    print(row)
cursor.close()
connection.commit()
connection.close()

print("Test database and table created successfully.")