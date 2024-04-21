class Student:
    def __init__(self,name,school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)   

    # the cls represents the class that is calling this method
    # since we don't have access to the self method we need to specify the origin as a parameter
    @classmethod
    def friend(cls,origin,friend_name,*args,**kwargs):
        return cls(friend_name,origin.school,*args,**kwargs)
    

# anna = Student("Anna","MIT")
# print(anna.name)
# friend = anna.friend("Ogolla")
# print(friend.name)
# print(friend.school)    
    


class workingStudent(Student):
    # use super to call the parent class
    def __init__(self, name, school,salary,job_title):
        super().__init__(name, school)
        self.salary = salary
        self.job_title = job_title


james = workingStudent("James","Stanford",20.00,"software developer")
print(james.salary)

# this cannot work because the Student doesn't have the property salary
# to make it work we must use the @classMethod so that we can use the workingStudent instance to call the function
jeff = workingStudent.friend(james,"Jeff",10.00,job_title = "software developer")
print(jeff.salary) 
print(jeff.school)
print(jeff.job_title)