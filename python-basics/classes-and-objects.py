class Dimensions:
    def __init__(self,length,width,height):
        self.length = length
        self.width = width
        self.height = height

    def perimeter(self):
        return 2*(self.length + self.width)

    def area(self):
        return self.length * self.width

    def volume(self):
        return  self.length * self.width * self.height    
    

#students details
class students:
    def __init__(self,name,school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)
    
    # Method 1
    # @classmethod
    # def go_to_school(cls):
    #     print("I am going to school")

    # Method 2
    # def got_to_school(self):
    #     print("I am going to school")  
    
    # Method 3
    @staticmethod
    def go_to_school():
        print("I am going to school")        
    
all_students = students("all_students","MIT")    
    
anna = students("anna","MIT")
all_students.marks.append(90)

bella = students("bella","MIT")
all_students.marks.append(75)

jose = students("jose","MIT")
all_students.marks.append(85)

son = students("son","MIT")
all_students.marks.append(65)

yu = students("yu","MIT")
all_students.marks.append(70)

# We pass the self parameter even if we're not using it.
# We can also use @classMethod keyword above the method and pass the parameter cls
# when we use @staticmethod keyword we cannot use a class object we need to use the class itself.
students.go_to_school()

print("The average marks of the students is :",all_students.average())
        