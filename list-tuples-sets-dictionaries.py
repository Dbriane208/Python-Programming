# lists are mutable
# tuples are immuatable
# sets contain unique & unordered items


list_grades = [45,90,78,56,98]
tuple_grades = (45,90,78,56,98)
set_grades = {45,90,78,56,98}

#adding a grade to each of them
list_grades.append(100)
#print(list_grades)

tuple_grades = tuple_grades + (100,) # we use a comma after the value we want to get
#print(tuple_grades)

set_grades.add(100)
#print(set_grades)

# updating the each of them
# we cannot update a tuple we can only access and concatenate
list_grades[0] = 67
#print(list_grades)


# Advanced set operations
lottery_numbers = {45,90,78,56,98}
winning_numbers = {90,56,23,10}

# # intersection - common numbers in both sets
# print(lottery_numbers.intersection(winning_numbers))
# # union - unique numbers from each set
# print(lottery_numbers.union(winning_numbers))
# # difference - numbers not in other set
# print(lottery_numbers.difference(winning_numbers))


#List comprehensions
list_of_numbers = [x for x in range(10) if x % 2 == 0]
#print(list_of_numbers)

# create a dictionary name called student
student = {
    "name" : "xyz",
    "school" : "Engineering",
    "grades" : (67,90,43,35)
}

# modify the grade variable so that it access the grades key
# assume the argument data is a dictionary
def average_grade(data):
    grades = data["grades"]
    return sum(grades) /len(grades)

# Implement the function below
# Given a list of students (dictionaries), calculate the average grade of the class
# You must add all the grades of all the students together
# You must also count how many grades there are in total in the entire list
def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
         total += sum(student["grades"])
         count += len(student["grades"])

    return total / count    