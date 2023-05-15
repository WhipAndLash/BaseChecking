# import sqlite3
# import os

# filename = "testing.db"

# # Delete existing databases

# # check if file exists
# if os.path.isfile(filename):
#     # delete file
#     os.remove(filename)
    
# # connecting to the database
# conn = sqlite3.connect('testing.db')

# # Prompt the user to set a password for the database
# password = input("Enter a password for the database: ")

# # Create a checkin table with a Name, Course, and Student-ID field
# c = conn.cursor()
# c.execute('''CREATE TABLE IF NOT EXISTS checkin
#              (Name TEXT, Course TEXT, Student_Id TEXT, List TEXT, Whitelist TEXT, Blacklist TEXT,  PRIMARY KEY (Name, Course, Student_Id, List))''')

# # IDs
# records = [('Diego', 'IMIT2', '1111', 'Whitelisted'),
#            ('Jack', 'IMST-IT2', '2222', 'Whitelisted'),
#            ('Bertine', 'IMIT2', '3333','Blacklisted'),
#            ('Theodor', 'IMST-IT2', '4444', 'Whitelisted'),
#            ('Isak', 'IMIT2', '5555','Blacklisted'),
#            ('Viktor', 'IMST-IT2', '6666', 'Whitelisted'),
#            ('Kristian', 'IMST-IT2', '7777', 'Whitelisted'),
#            ('Alice', 'IMST1', '8888','Blacklisted'),
#            ('Fred', 'IM1', '9999','Blacklisted'),
#            ('Eva', 'IMST1', '0000','Blacklisted')]

# # Insert the records into the checkin table
# c.executemany("INSERT INTO checkin (Name, Course, Student_Id, List) VALUES (?, ?, ?, ?)", records)

# # Commit the changes and close the connection
# conn.commit()
# conn.close()


# As made in heave suggests, im deleting everything and starting from zero!

