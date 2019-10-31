def func1(aList):
    aList.append('Eric')

def main():
    # Create a list of students
    students = ['Bruce','Gayle','Tucker','Bella']
    print("Initial list values;",students)
    func1(students)
    print("New list values after calling func1 function:",students)

    print()
    print()
    """
    Students was mutable since when you pass in a list to a funcito you
    are passing in a reference to the data and not the actually date.
    This is way it's mutable.

    So now lets make a copy of the original list before calling the function
    """
    
    # Create a list of students
    students = ['Bruce','Gayle','Tucker','Bella']

    # Copy the list. Note the [:]
    copyOfStudents = students[:] #slicing
    # copyOfStudents = list(students)

    print("List values copied from students into copyOfStudents;",copyOfStudents)
    func1(copyOfStudents)
    print("Copy of students was mutated:",copyOfStudents)

    print("But not the original students list still in tact:",students)

main()        
