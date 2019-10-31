

def main():
     # create new students list
     students = []

     # ask how many students to enter
     studentCount = eval(input("How many students will you be entering? "))

     for i in range(studentCount):
          # ask for a nuame
          newName = input("Enter a students name: ")

          students.append(newName)

     # add a student Sam
     students.insert(1,"Sam")

     # grab last student name
     theEnd = students.pop()

     students.sort()

     students.remove("Sam")

     for student in students:
          print(student)

main()

     
