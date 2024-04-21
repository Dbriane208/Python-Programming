def methodception(another):
    return another()

def add_two_numbers():
    return 35 + 77

# # Method 1
print(methodception(add_two_numbers))

# Method 2
# we can use lambda to print the result
print(f"Using lambda : {methodception(lambda : 35 + 77)}")

my_list = [13,56,77,84]
print(list(filter(lambda x: x != 13, my_list)))

even_list = [45,90,35,8,76,0,13,43]
x = list(filter(lambda x: x % 2 == 0, even_list))
print(x)

# using list  comprehensions to achieve the same goal
result = [x for x in even_list if x % 2 == 0]
print(result)