# MySQL-Connector
This Python script facilitates the import of data from CSV (Comma-Separated Values) files into a MySQL database. It leverages the mysql.connector library to establish a connection with the MySQL database and uses standard CSV parsing techniques to read data from the input file.

CSV to MySQL Import Script
This Python script enables the import of data from CSV (Comma-Separated Values) files into a MySQL database. It utilizes the mysql.connector library to establish a connection with the MySQL database and inserts parsed data from the CSV file into a designated table.

---Key Features---
CSV Data Parsing: Reads data from a specified CSV file (products.csv) and extracts relevant attributes such as SKU, item name, specifications, and price.
MySQL Database Interaction: Establishes a connection with a MySQL database (test in this example) and inserts parsed data into a designated table (items).
Data Insertion: Processes each row of data from the CSV file and inserts it into the MySQL database using parameterized SQL queries to ensure secure and efficient data insertion.

****Usage****

1.Setup:
Ensure Python and the required libraries (mysql.connector and csv) are installed.
Modify the script (csv_to_mysql_import.py) to specify your MySQL database credentials (host, user, password, database, port).

2.CSV File Format:
Prepare a CSV file (products.csv) containing data organized in columns (e.g., SKU, item name, specifications, price).
Running the Script:
Execute the script to read data from the CSV file and insert it into the MySQL database.
------>python csv_to_mysql_import.py


****Requirements****

1.Python 3.x

2.mysql.connector library

3.csv library (standard library in Python)
