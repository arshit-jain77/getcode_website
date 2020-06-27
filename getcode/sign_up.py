import sqlite3
# from flask import request

conn = sqlite3.connect('sign_up.sqlite')
cur = conn.cursor()

def store_data(conn, Data):
    """Store a new Data in the database(Data)"""

    First = input("Enter First name:")
    Last = input("Enter last name:")
    while(True):
        Pno = input("Enter your Phone number:")
        if len(Pno)!=10: print("!!Phone number must be of 10 digits!!") 
        else: break
    while(True):
        email=input("Enter email address:")
        if '@' not in email: print("!!Invalid email address!!")
        else: break
    Pass=input("Enter password:")
    
    cur = conn.cursor()
    cur.execute("INSERT INTO Data (FirstName, LastName, PhoneNumber, Email, Password) VALUES (?)", (First, Last, Pno, email, Pass))
    conn.commit()

cur.execute('DROP TABLE IF EXISTS Data')
cur.execute('''CREATE TABLE Data (FirstName TEXT,LastName TEXT,PhoneNumber TEXT,Email TEXT,Password TEXT)''')

# store_data(conn,request.forms.get('Data'))

cur.close()

def get_data(conn):
   """Return a list of Email and Password from the database(Data)"""

   cur = conn.cursor()
   cur.execute("SELECT Email,Password FROM Data")
   emails = []
   passwords = []
   for row in cur:
       emails.append(row['Email'])
       passwords.append(row['Password'])
   return emails,passwords    