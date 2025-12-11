import mysql.connector

try:
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password= "root",
        database = 'TestDatabase'
    )
    cursor = conn.cursor()
    print("Connected to MySQL database successfully!")

except mysql.connector.Error as err:
    print(f"Error connecting to MySQL: {err}")

#Read Record or fetch record
select_query = "SELECT * FROM persons WHERE PersonID = %s"
user_id = 1

try:
    cursor.execute(select_query, (user_id,))
    record = cursor.fetchone()
    if record:
        print(f"User found: PersonID={record[0]}, FirstName={record[1]}, LastName={record[2]}, Address={record[3]}, City={record[4]}")
    else:
        print("User not found.")
except mysql.connector.Error as err:
    print(f"Error reading record: {err}")

#Insert Query
# Table named 'persons' with columns 'PersonID', 'FirstName', 'LastName', 'Address', 'City'
insert_query = "INSERT INTO persons (PersonID, FirstName, LastName, Address, City) VALUES (%s, %s, %s, %s, %s)"
user_data = (4,"John", "Doe", "abc 26", "New York")

try:
    cursor.execute(insert_query, user_data)
    conn.commit()
    print("Record inserted successfully!")
except mysql.connector.Error as err:
    conn.rollback()
    print(f"Error inserting record: {err}")

   
#Update Query:
# Table named 'persons' please mention name of the column which you have to update.
# In this case I am updating Address Column
update_query = "UPDATE persons SET Address = %s WHERE PersonID = %s"
new_Address = "xyz 20"
user_id = 4

try:
    cursor.execute(update_query, (new_Address, user_id))
    conn.commit()
    print("Record updated successfully!")
except mysql.connector.Error as err:
    conn.rollback()
    print(f"Error updating record: {err}")

#Delete the record:
delete_query = "DELETE FROM persons WHERE PersonID = %s"
user_id_to_delete = 5

try:
    cursor.execute(delete_query, (user_id_to_delete,))
    conn.commit()
    print("Record deleted successfully!")
except mysql.connector.Error as err:
    conn.rollback()
    print(f"Error deleting record: {err}")

if conn.is_connected():
    cursor.close()
    conn.close()
    print("MySQL connection closed.")


