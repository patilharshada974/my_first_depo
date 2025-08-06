# Import required libraries
import psycopg2  # For PostgreSQL database connection
import sys  # For exiting the program cleanly


# Function to establish a connection with the PostgreSQL database
def connect_db():

    connection = psycopg2.connect(
        user="postgres",  # Username for PostgreSQL
        password="******",  # Password for PostgreSQL
        host='localhost',  # Host address (127.0.0.1 or localhost)
        port="5432",  # Default PostgreSQL port
        database='postgres'  # Name of the database to connect to
    )
    return connection


# Function to create a new table using the provided SQL query
def create_table_into_db(query):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute(query)  # Executes the create table query
    print("✅ Table created successfully.")
    connection.commit()  # Save the changes to the database
    cursor.close()
    connection.close()


# Function to insert data into the table using the provided SQL query
def insert_data_into_db(query):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute(query)  # Executes the insert query
    print("✅ Data inserted successfully.")
    connection.commit()
    cursor.close()
    connection.close()


# Function to read and display all records from the homemade_product table
def read_data_from_db():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM homemade_product")  # Fetch all data
    results = cursor.fetchall()  # Get all rows
    print("\n📋 Table Data:")
    for row in results:
        print(row)  # Display each row
    connection.commit()
    cursor.close()
    connection.close()


# Function to drop (delete) the table if it exists
def drop_table_from_db():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS homemade_product")  # Drop table
    print("❌ Table dropped successfully.")
    connection.commit()
    cursor.close()
    connection.close()


# ---------------- Main menu loop ----------------
while True:
    # Display options to the user
    print("\n" + "-" * 75)
    print("1. Create table in DB")
    print("2. Insert data into table")
    print("3. Read data from table")
    print("4. Drop table from DB")
    print("5. Exit")

    # Ask user for input
    choice = input("Enter your choice (1-5): ")

    # Perform actions based on user choice
    if choice == '1':
        # SQL query to create table
        query_create = """
                       CREATE TABLE homemade_product 
                       ( 
                           p_id    INT, 
                           p_name  VARCHAR(20), 
                           p_price FLOAT
                       ) 
                       """
        create_table_into_db(query_create)

    elif choice == '2':
        # SQL query to insert multiple rows of data
        query_insert = """
                       INSERT INTO homemade_product 
                       VALUES (1875678, 'Termind', 86.34), 
                              (1125447, 'Garam Masal', 100.36), 
                              (8457123, 'Chilli Powder', 200.65), 
                              (1475682, 'Tea Powder', 180.57) 
                       """
        insert_data_into_db(query_insert)

    elif choice == '3':
        # Read and display all data from the table
        read_data_from_db()

    elif choice == '4':
        # Drop the table if it exists
        drop_table_from_db()

    elif choice == '5':
        # Exit the program
        print("👋 Program exited.")
        sys.exit(0)

    else:
        # Handle invalid menu choices
        print("⚠️ Please enter a valid choice (1-5).")












