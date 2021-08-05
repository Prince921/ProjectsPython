print('Welcome to this Grade Sorter Porgram')
name = input('What is your name?').title().strip()
print('Hello '+name+'!')
no_of_student = int(input("Enter number of Students"))
grades = []
for i in range(no_of_student):
    grade = int(input('Enter grade of '+str(i)+'th student'))
    grades.append(grade)
print('The unsorted grades are : '+str(grades))
grades.sort(reverse=True)
print('Sorted Highest to lowest : '+str(grades))
