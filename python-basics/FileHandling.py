import os

# opening a file
def openFile(filename,mode):
    try:
     with open(filename,mode) as name_file:
        return name_file
    except FileNotFoundError as fnf_error:
       print(f"File {fnf_error} is not found.")


# writing a file
def writeFile(filename,mode):
    try:
        with open(filename,mode) as file_name:
           content = "Mark Daniel Gatuhu"
           output = file_name.write(content)
           return output
    except FileNotFoundError as fnf_error:
       print(f"File {fnf_error} is not found.")    

# reading a file
def readFile(filename,mode):
    try:
        with open(filename,mode) as output:
           return print(output.read())
    except FileNotFoundError as fnf_error:
       print(f"File {fnf_error} is not found.")    

# delete the file
def deleteFile(filename):
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print(f"The file {filename} does not exist.")    

# calling the funcitons
openFile('name.txt','r')
writeFile('name.txt','w') 
readFile('name.txt','r') 
deleteFile('names.txt')