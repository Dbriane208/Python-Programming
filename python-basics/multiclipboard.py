#Importing the packages we need
import sys
import clipboard
import json

SAVED_DATA = 'clipboard.json'

def save_data(filepath,data):
    with open(filepath,'w') as f:
        json.dump(data,f)

def load_data(filepath):
    try:
        with open(filepath,'r') as f:
            data_loaded = json.load(f)
            return data_loaded  
    except:
        return {}    
     
    
if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == 'save':
        key = input('Enter a key : ')
        data[key] = clipboard.paste()
        save_data(SAVED_DATA,data)
        print('Data saved!')

    elif command == 'copy':
        key = input('Enter a key : ')
        if key in data:
            clipboard.copy(data[key])
            print('Data copied to clipboard!')
        else:
            print('Key does not exist') 

    elif command == 'list':
        print(data)        

    elif command == 'clear':
        data.clear()        
        save_data(SAVED_DATA,data) 
        print("Data on clipboard deleted!") 
    else:
        print('unknown command')
else:
    print('The length should be exactly two')                
    
    
