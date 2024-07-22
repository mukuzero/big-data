import cx_Oracle

# Connection details
username = "c##hr"
password = "hr1"
host = '34.134.232.252'
port = '1521'
service = 'ORCLCDB'

dsn =f"{host}:{port}/{service}"
# query="ALTER SESSION SET NLS_DATE_FORMAT = 'YYYY-MM-DD'"

query="select * from project_details_data"

source_connection = cx_Oracle.connect(username, password, dsn)
# Create a cursor object to execute the SQL queries
cursor = source_connection.cursor()


t=cursor.execute(query)

print(t.fetchall())
# Commit the changes
source_connection.commit()

# Close the cursor and connection
cursor.close()
source_connection.close()

print("DDL statements executed successfully.")