# if statements
known_people = ["John","James","Smith"]

#introduction
intro = input("Welcome to names db. Would you like to proceed (y/n/q): ")
if intro == "y":
    person = input("Enter the name of person you know : ")
    person_db = person[0].upper() + person[1:]

    if person_db in known_people:
       print(f"There is a person called: {person_db} in our database!")
    else:
      print(f" There is no person such : {person_db} in our database!")   
elif intro == "n":
   print("Thank you! see you soon.")
elif intro == "q":
   print("You Quited the program!")           


## Given a list return even numbers
def even_numbers(list):
    db_even = []
    for nums in list:
        if nums % 2 == 0:
            db_even.append(nums)
    for num in db_even:
        print(num)    

list = [23,45,24,90,44,68,77]
even_numbers(list)



# Exercise
def who_do_you_know():
    person = str(input("Enter the name of a person you know separated by a comma: "))
    person_without_spaces = [name.strip() for name in person.split(',')]

    # person_list = person.split(',')
    # for people in person_list:
    #     person_without_spaces.append(people.strip())

    return person_without_spaces

def ask_user():
    list_name = str(input("Enter a name you know: "))
    if list_name in who_do_you_know():
        print(f"You know {list_name} who is in your list of names!")
    else:
        print(f"You don't know a person in your list of names!")    

ask_user()