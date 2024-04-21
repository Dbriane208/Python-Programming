import functools

# decorators that doesn't accept arguments
def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print("In the decorator")
        func()
        print("After the decorator")
        return function_that_runs_func
    
@my_decorator
def my_function():
    print("I'm the function!")

my_function  

# decorators that accepts arguments
def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        # this function replaces my_funciton_too when the decorator function is run
        def function_that_runs_func(*args,**kwargs):
            print("In the decorator")
            if number == 56:
                print("Not running the function")
            else:
                func(*args,**kwargs)
            print("After the decorator!")
        return function_that_runs_func
    # returns the decorator to apply the funct_that_runs_func get applied
    return my_decorator


@decorator_with_arguments(57)
def my_function_too(x,y):
    print(x + y)

my_function_too(57,90)    

