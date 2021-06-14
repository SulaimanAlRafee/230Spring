import code

code.add_4_students()
cont = 1
while cont > 0:
  code.print_menu()
  cont = int(input("Select a number:"))
  if cont == 1:
    code.print_all_students()
  elif cont == 2:
    code.add_student()
  elif cont == 3:
    code.print_by_major()
  elif cont == 4:
    code.print_warnings()
  elif cont == 5:
    print("Average GPA =",code.print_avg_gpa())
