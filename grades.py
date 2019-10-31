# demo of creating a list of grades
# getting lowest and highest scores from it

# create list to hold grades
grades = []

# add 5 grades to the list
for i in range(5):
    # get input as string
    grade = input("Grade? ")
    # append to list and force to float
    grades.append(float(grade))

# sort the grades
grades.sort()

# get lowest one
print(grades[0])
# get highest one
print(grades[-1])

