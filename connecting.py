import sqlite3

# Re-connect to the database with the password
while True:
    pwd = input("Enter the database password: ")
    try:
        conn = sqlite3.connect('testing.db')
        conn.execute(f"PRAGMA key = '{pwd}';")
        break
    except:
        print("Invalid password, please try again.")

# Query the checkin table and print the results
c = conn.cursor()
c.execute("SELECT * FROM checkin")
rows = c.fetchall()
for row in rows:
    print("Name:", row[0])
    print("Course:", row[1])
    print("Student-Id:", row[2])
    print("List:", row[3])
    print("")

# Close the database connection
# conn.close()
