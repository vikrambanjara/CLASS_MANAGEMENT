import sqlite3

connection=sqlite3.connect('classmangementsystem.db')
cursor= connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS STUDENTS
               (
                NAME TEXT NOT NULL,
                FATHER_NAME TEXT NOT NULL,
                MOTHER_NAME TEXT NOT NULL,
                MOBILE_NO INT NOT NULL UNIQUE,
                IDENTITY_CARD TEXT NOT NULL,
                STUDENT_FEES INT NOT NULL
                
               )""")


def add_student(data):
  check=cursor.execute("INSERT INTO STUDENTS VALUES(?,?,?,?,?,?)",data)
  connection.commit()
  if check:
    return True
  return False
     
def get_student(NAME):
   cursor.execute("SELECT * FROM STUDENTS WHERE NAME=(?)",(NAME,))
   check=cursor.fetchone()
   return check
   

def DELETE_STUDENT(NAME):
     if get_student(NAME):
        cursor.execute("DELETE FROM STUDENTS WHERE NAME =(?)",(NAME,))
        connection.commit()
        return True
     return False

def IDENTITY_CARD(NAME):
    cursor.execute("SELECT IDENTITY_CARD FROM STUDENTS WHERE NAME=(?)",(NAME,))
    Cheak=cursor.fetchone()
    return Cheak
     
  

def STUDENT_FEES(NAME):
   cursor.execute("SELECT STUDENT_FEES FROM STUDENTS WHERE NAME =(?)",(NAME,))
   Cheak=cursor.fetchone()
   return Cheak
  