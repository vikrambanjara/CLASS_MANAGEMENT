import models

def admin_log_in(user_name,password):
  if user_name=='student' and password=='student01':
    return True
  return False

def Cheak_student(data):
  if models.add_student(data):
        print("Add Student Successfully")
  else:
    print("Student is not Add")
