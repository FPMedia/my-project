# Import a Python Database API-2.0-compliant interface.
import mysql.connector

# Open a connection to the database
connection = mysql.connector.connect(
    host='lahman.csw1rmup8ri6.us-east-1.rds.amazonaws.com',
    user='python',
    passwd='python',
    db='lahmansbaseballdb'
)

# Write your query. For example, this query will get the first and last names, weight, and year of debut for the heaviest five people in the people table:
query = """SELECT nameFirst, nameLast, weight, year(debut)
  FROM people
  ORDER BY weight DESC
  LIMIT 5
"""

# Create a cursor for the connection:
cursor = connection.cursor()

# Use the cursor to execute one or more queries:
cursor.execute(query)

# Get the results of the query/queries from the cursor:
results = cursor.fetchall()

# Do something with the results. Here we just output the results:
print(results)

# Close the cursor:
cursor.close()

# Close the connection to the database:
connection.close()