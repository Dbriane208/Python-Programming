## creating a method
def Car(color):
    model = "Benz"
    year_of_manufacture = 2023
    #we print the output
    print(f"The {color} car is a {model} and was manufactured in {year_of_manufacture}.")

# ## we call the car method
# Car("Blue")


## method that takes two arguments
def Calculator(num1, num2,operator):
    if operator == "+":
        return print(f"The sum is : {num1 + num2}")
    elif operator == "-":
        return print(f"The difference is : {num1 - num2}")
    elif operator == "*":
        return print(f"The multiplication is {num1 * num2}")
    elif operator == "/":
        return print(f"The division is {num1 / num2}")
    else:
        return f"Invalid output"

# oper = input("Choose an operator between +,-,*,/ : ")
# Calculator(5,2,oper)

## using list
# sort the list using bubble sort
def sort_grades(grades):
    for value in range(len(grades)-1,0,-1):
        for grade in range(value):
            if grades[grade] > grades[grade + 1]:
                # swap
                temp = grades[grade]
                grades[grade] = grades[grade + 1]
                grades[grade + 1] = temp

# grades = [89,23,78,45,10]             
# sort_grades(grades)
# print(grades)
                
## implementing the sum data structure
def list_sum(list):
    for value in range(len(list)):
        for element in range(value+1,len(list)):
            sum = list[value] + list[element]
            print(f"The sum of {list[value]} and {list[element]} is {sum}")
        
        
# grades = [89,23,78,45,10] 
# list_sum(grades)

def no_sum(list):
    total_sum = sum(list)
    current_sum = 0
    index = 0

    while current_sum != total_sum:
        current_sum += list[index]
        print(f"Current sum :{current_sum}")
        index += 1

# grades = [89,23,78,45,10]             
# no_sum(grades)     

def list_sum(list):
    total_sum = 0
    for num in list:
        total_sum += num
    print(total_sum)

list_numbers = [89,23,78,45,10] 
list_sum(list_numbers)



