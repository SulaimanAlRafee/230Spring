class Bank_Account:
  def __init__(self, name_of_holder, type_of_account, beginning_balance):
    self.holder_name = name_of_holder
    self.account_type = type_of_account
    self.balance = beginning_balance

  def print_account_info(self):
    print('-----Account Info-----')
    print('Name =',self.holder_name)
    print('Type =',self.account_type)
    print('Balance =',self.balance)
    print('----------------------\n')

  def deposit(self,how_much_money):
    self.balance = self.balance + how_much_money
    print('-----Depositing-----')
    print("Just deposited",how_much_money)
    print('----------------------\n')

  def withdraw(self,how_much_money):
    if how_much_money > self.balance:
      print("Sorry, you don't have that much money\n")
    else:
        self.balance = self.balance - how_much_money
        print('-----Withdrawing-----')
        print("Just withdrawn",how_much_money)
        print('----------------------\n')

customer_name = input("Enter customer name:")
account_type = input("Enter account type:")
beginning_balance = int(input("Enter balance at the start:"))

new_account = Bank_Account(customer_name,account_type,beginning_balance)

new_account.print_account_info()

cont = 'y'
while cont == 'y':
  operation = input("What operation (D/W):")
  how_much_money = int(input("How much money:"))
  if operation == 'D':
    new_account.deposit(how_much_money)
  else:
    new_account.withdraw(how_much_money)
  new_account.print_account_info()
  cont = input("Want to continue:")

# class Student:
#   def __init__(self,s_name, s_id, s_major):
#     self.name = s_name
#     self.id = s_id
#     self.major = s_major

#   def print_student_info(self):
#     print('----------------')
#     print('Name =', self.name)
#     print('ID =',self.id)
#     print('Major =',self.major)
#     print('----------------')

# # this is the new way
# new_student = Student('Sulaiman Ali','13332123',"MIS")
# new_student.print_student_info()
# new_student1 = Student('Sarah Ahmed','9999999999','Finance')
# new_student1.print_student_info()
# new_student2 = Student('Jassim Hassan','77777777777','Computer Science')
# new_student2.print_student_info()
# # this is the old way
# # new_student = Student()
# # new_student.name = "Sulaiman ali"
# # new_student.id = "23423423434"
# # new_student.major = "MIS"
# # new_student1 = Student()
# # new_student1.name = "Jassim Hasan"
# # new_student1.id = "11111111111"
# # new_student1.major = "Computer Science"
