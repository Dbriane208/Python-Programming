# args takes a list of elements
def names(*args):
    return print(args)

# names("John","James","Mary","Susan",70,80)

# kwargs takes key-word arguments
def key_names(name,**kwargs):
    return print(name)

# key_names("son") - this would return an empty set
#key_names(name="son")


# we can also use both args and kwargs together
def exam(*args,**kwargs):
    return print(args,kwargs)

exam("Jeremy","Henry","Juma",80,90,90,subject="Maths",score= 98)
