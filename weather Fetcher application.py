#Used to enquire data from an endpoint
import requests

#Ap key and base url
API_KEY = "09e4b080acb40b8de56323d29705d4fc"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Getting the city we want information about
city = input("Enter a city : ")

# Helping us to get the data of the city together with the api key
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

# Using get to retrieve information from the server
response = requests.get(request_url)

# Sometimes the response might have an error so we have to handele it
if response.status_code == 200 :

    data = response.json()

    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp']  - 273.15,2)
  
    print('The weather is : ',weather) 
    print('The temperature is : ',temperature,' degree celcius')  

else:
    print("An error occured")
