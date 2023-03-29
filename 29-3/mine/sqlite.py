import sqlite3

# Create a connection to the database
con = sqlite3.connect('internetSpeed.db')

# create a curser object
cursor = con.cursor()

# Get the names of the tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table';")
tables = cursor.fetchall()

# Print the table name
for table in tables:
    print(table[0])

""" # Execute a SQL command
cursor.execute('SELECT * FROM LA_wifi_speed_UK')

# Fetch the results
results = cursor.fetchall() """

# Close the Cursor and the Connection
cursor.close()
con.close()