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

# intersection - common numbers in both sets
print(lottery_numbers.intersection(winning_numbers))
# union - unique numbers from each set
print(lottery_numbers.union(winning_numbers))
# difference - numbers not in other set
print(lottery_numbers.difference(winning_numbers))


