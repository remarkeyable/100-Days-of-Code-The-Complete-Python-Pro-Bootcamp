import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('/instance/task.db')
cursor = conn.cursor()

# Specify the table name and column(s) to fetch
table_name = 'your_table'
column_name = 'your_column'

# Execute a query to retrieve the specific column from the table
cursor.execute(f'SELECT {column_name} FROM {table_name}')

# Fetch all the rows from the query result
rows = cursor.fetchall()

# Convert the rows into a list
data_list = [row[0] for row in rows]

# Close the cursor and the connection
cursor.close()
conn.close()
