import controler
import models


def admin_func():
  print("Enter 1 for Add Stuents")
  print("Enter 2 for Delete Student")
  print("Enter 3 for Cheak Identity card")
  print("Enter 4 for Student Fees")
  print("Enter any number for EXIT ")


def admin_func_key(choice):
  if choice==1:
    add_student()
  elif choice==2:
    delete_student()
  elif choice==3:
    Cheak_identity_card()
  elif choice==4:
    student_fees()
  else:
    print("INVALID CHOICE")


def add_student():
  NAME=input("Enter Student Name: ")
  FATHER_NAME=input("Enter Father Name: ")
  MOTHER_NAME=input("Enter Mother Name: ")
  MOBILE_NO=input("Enter Moblie no.: ")
  IDENTITY_CARD=input("Enter IDENTITY_CARD  (Yes or No): ")
  STUDENT_FEES=input("Enter Student Fees: ")
  data=(NAME,FATHER_NAME,MOTHER_NAME, MOBILE_NO,IDENTITY_CARD,STUDENT_FEES)
  controler.Cheak_student(data)

def delete_student():
  NAME=input("Enter Student Name: ")
  if models.DELETE_STUDENT(NAME):
    print("Student Detail Deleted")
  else:
    print("Student Not Exists")

def Cheak_identity_card():
  NAME=input("Enter your Name: ")
  data=models.IDENTITY_CARD(NAME)
  print("This Student name {} Identity_card is {} ".format(NAME,data))
  
  
def student_fees():
  NAME=input("Enter Student Name: ")
  data=models.STUDENT_FEES(NAME)
  print("student name {} and fees is {}".format(NAME,data[0]))




def main():
  user_name= input("Enter your user_name: ")
  password=input("Enter your password: ")
  if controler.admin_log_in(user_name,password):
    print("WELCOME TO CLASS MANAGEMENT SYSTEM")
    admin_func()
    choose=int(input("Enter a Number: "))
    admin_func_key(choose)
  else:
    print("Oops! Your username or password is wrong.")


main()