import mysql. connector
import csv

# Connect to the MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='test',
    port=3306
)

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Read data from a CSV file (replace with your data source)
with open('C:/Users/91860/OneDrive/Documents/products.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip header row if applicable

    for row in csv_reader:
        print(row)
        # Process and extract attributes from the row as needed
        sku = row[0]
        item = row[1]
        specs = row[2]
        price = row[3]

        # Insert data into the MySQL database
        cursor.execute('INSERT INTO items (sku, item, specs, price) VALUES (%s, %s, %s, %s)', (sku, item, specs, price))

# Commit changes and close connections
connection.commit()
cursor.close()
connection.close()
