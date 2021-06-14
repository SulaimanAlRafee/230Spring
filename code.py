students = []

class Student:

  def __init__(self, name, major, GPA):
    self.name = name
    self.major = major
    self.GPA = GPA
  
  def print(self):
    print("\nStudent information")
    print("------------")
    print("Name: ",self.name)
    print("Major: ",self.major)
    print("GPA: ",self.GPA)
    print("------------\n")

def print_all_students():
  for a_student in students:
    a_student.print()

def add_4_students():
  students.append(Student('Ahmed','MIS',2.1))
  students.append(Student('Sarah','Finance',2.3))
  students.append(Student('Yousef','Accounting',1.8))
  students.append(Student('Khalid','MIS',3.4))

def print_menu():
  print("1. print all students")
  print("2. add a student")
  print("3. students by major")
  print("4. students with warning")
  print("5. average GPA for students")
  print("0. exit")

def add_student():
  s_name = input("Enter student name:")
  s_major = input("Enter student major:")
  s_GPA = float(input("Enter student GPA:"))
  students.append(Student(s_name, s_major, s_GPA))

def print_by_major():
  major = input("What major do you want:")
  for a_student in students:
    if a_student.major == major:
      a_student.print()
  
def print_warnings():
  for a_student in students:
    if a_student.GPA < 2:
      a_student.print()

def print_avg_gpa():
  total_gpa = 0
  for a_student in students:
    total_gpa = total_gpa + a_student.GPA
  avg_GPA = total_gpa / len(students)
  return avg_GPA
