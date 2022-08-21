import psycopg2

try:
    connection = psycopg2.connect(
        user="postgres",
        password="mft2022",
        host="127.0.0.1", # localhost
        port="5432",
        database="advanced"
    )
    cursor = connection.cursor()
    #cursor.execute("SELECT ID, NAME, SALARY FROM COMPANY;")
    # query = """SELECT NAME, MAX(SALARY) FROM COMPANY GROUP BY NAME ORDER BY NAME DESC LIMIT 2;"""
    # query = """SELECT NAME, SALARY FROM COMPANY ORDER BY NAME DESC LIMIT 2;"""
    query = """SELECT NAME, SALARY FROM COMPANY ORDER BY NAME DESC LIMIT 2;"""

    cursor.execute(query)
    # record = cursor.fetchone()
    records = cursor.fetchall()
    
    for record in records:
        print(record)

    # print("You are connected to - ", record, "\n")

except Exception as e:
    print(e)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")