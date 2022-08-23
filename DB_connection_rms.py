'''
This Program is used to connect to the database to get the data for analysis and to examine the database records
to check if there are any updates or inserts required as per the admin users and view the existing data
'''

import mysql.connector
from mysql.connector import errorcode

#This method gets the table name from the user.
def get_details():
    statuses = {1: "customer", 2: "menu", 3: "orders", 4: "payment", 5: "reservation", 6: "staff"}
    print("Please select table name required for view")
    for key in statuses:
        print("{}. {}".format(key, statuses[key]))

    status = int(input("Enter status number for table"))
    if 0 < status <= 6:
        return statuses[status]
    else:
        return "Please enter a valid option"


try:
#Creating connection to the database
   cm_connection = mysql.connector.connect(
      user="root",
      password="root",
      host="127.0.0.1",
      database="restaurant_managment_system")
#exception handling
except mysql.connector.Error as err:
   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Invalid credentials")
   elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database not found")
   else:
      print("Cannot connect to database:", err)

else:
   # Execute database operations...
   print("Sucessfully connected to database")

   #get which table details are required.
   tbl_details = str(get_details())

   if tbl_details == 'Please enter a valid option':
      print(tbl_details)
   else:
      # Creating a Cursor
      my_cursor = cm_connection.cursor()
      select_query = ''
      if tbl_details == 'customer':
         # Select query for getting the required data from customer table.
         select_query = ("select * from customer limit 3")
      if tbl_details == 'menu':
         # Select query for getting the required data from menu table.
         select_query = ("select * from menu limit 3")
      if tbl_details == 'orders':
         # Select query for getting the required data from orders table.
         select_query = ("select * from orders limit 3")
      if tbl_details == 'payment':
         # Select query for getting the required data from payment table.
         select_query = ("select * from payment limit 3")
      if tbl_details == 'reservation':
         # Select query for getting the required data from reservation table.
         select_query = ("select * from reservation limit 3")
      if tbl_details == 'staff':
         # Select query for getting the required data from restaurant_staff table.
         select_query = ("select * from restaurant_staff limit 3")

      #executing the select Query using cussor
      my_cursor.execute(select_query)
      #Looping throught the data from the cursor execution
      print("Results from select to console")
      for row in my_cursor.fetchall():
         print(row)

      #closing the cursor
      my_cursor.close()
   #closing the connection
   cm_connection.close()

