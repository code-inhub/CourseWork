import mysql.connector as sql

try:
    conn = sql.connect(
    user = "root",
    password = "*****",
    host = "localhost",
    port = "3306"
    )
    
except:
    print("Can't connect")

else:
    print("Connected")
    
    cur = conn.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS PythonLab")
    cur.execute("USE PythonLab")

    try:
        cur.execute("""CREATE TABLE IF NOT EXISTS Employee (
            First_Name CHAR(20) NOT NULL,
            Last_Name CHAR(20),
            Age INT,
            Gender CHAR(1),
            Department CHAR(20),
            Income FLOAT
        )""")
        
    except Exception:
        print("Table not created")
        
    else:
        print("\nTable created")
        
        cur.execute("""INSERT INTO Employee values
                       ('Anshul', 'Rana', 20, 'M', 'IT', 50000.0),
                       ('sun', 'Smith', 28, 'F', 'HR', 45000.0),
                       ('JAZK', 'Johnson', 35, 'M', 'Finance', 60000.0)""")
        cur.execute("SELECT * FROM Employee")
        for data in cur: 
            print(data)

    cur.close()
    conn.close()