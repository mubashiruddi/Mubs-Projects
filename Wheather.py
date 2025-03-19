from weatherbit import Api
import json
import requests
import string

api="182380700c474bf09bda6a99ef3f5850"

#Input User
search=input("Search with ""City or Postal code""= ")

#Url configuration
url='http://api.weatherbit.io/v2.0/forecast/hourly?'

if search in "":
    print('Invalid Input')
else :
    #condition of postasl or city
    if search[0] in string.ascii_letters:
        url2=(url +'city=' + search + '&key=' + api)

    elif search[0] in string.digits:
        url2=(url + '&postal_code=' + search + '&key=' + api)
    
    #Implementation
    response = requests.get(url2)
    #Error Handling
    if response.status_code == 404:

        print('No city or postal code found')
        
    else:
        temp=response.json()['data'][0]['temp']
        weather=response.json()['data'][0]['weather']['description']
        Humidity=response.json()['data'][0]['rh']
        city_name=response.json()['city_name']

    #Print/Output 
        print(f'Temperature of {city_name} is {temp}')
        print(f'Weather condition of {city_name} is {weather}')
        print(f'Humidity condition of {city_name} is {Humidity}')