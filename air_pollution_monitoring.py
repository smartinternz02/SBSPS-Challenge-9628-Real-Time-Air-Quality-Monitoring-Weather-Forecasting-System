#AIR POLLUTION MONITORING PROJECT

#Importing Request Libary

import requests

#Extracting Data of Specified Place Using Weather API

city="Chennai"

url = 'http://api.airvisual.com/v2/city?city=Chennai&state=Tamil Nadu&country=India&key='

api_key = 'd8f18136-2624-4b9a-be84-228c2146e8b2' 

main_url = url + api_key

r = requests.get(main_url)

data = r.json()

#Finding Air Quality Range

def AQI(aqi):
    
    if (aqi>=0 or aqi<=50):
        return print("AQI : ",aqi,"Good")
        
    elif (aqi>=51 or aqi<=100):
        return print("AQI : ",aqi,"Satisfactory")
        
    elif (aqi>=101 or aqi<=200):
        return print("AQI : ",aqi,"Moderate")
        
    elif (aqi>=201 or aqi<300):
        return print("AQI : ",aqi,"Poor")
        
    elif (aqi>=301 or aqi<=400):
        return print("AQI : ",aqi,"Very Poor")
        
    else:
        return print("AQI : ",aqi,"Severe")

#Finding Main Air Pollutant

def switch(mainus):
    if (mainus=="p2"):
      print("Main Air Pollutant : Particulate Matter pm2.5")

    elif (mainus=="p1"):
      print("Main Air Pollutant : Particulate Matter pm10",)
    
    elif (mainus=="o3"):
      print("Main Air Pollutant : Ozone O3")

    elif (mainus=="n2"):
      print("Main Air Pollutant : Nitrogen dioxide NO2")

    elif (mainus=="s2"):
      print("Main Air Pollutant : Sulfur dioxide SO2")

    elif (mainus=="co"):
      print("Main Air Pollutant : Carbon monoxide CO")

#Getting Details of the Specified Place from the Data

city = data.get('data')['city']

state = data.get('data')['state']

country = data.get('data')['country'] 

coordinates = data.get('data')['location']['coordinates']

time_standard = data.get('data')['current']['pollution']['ts']

humidity = data.get('data')['current']['weather']['hu']

aqius = data.get('data')['current']['pollution']['aqius']

mainus = data.get('data')['current']['pollution']['mainus']

temp = data.get('data')['current']['weather']['tp']

precipitation = data.get('data')['current']['weather']['pr']

wind_speed = data.get('data')['current']['weather']['ws']

wind_direction = data.get('data')['current']['weather']['wd']

#Displaying Air Quality Monitoring System

print("*********************** AIR QUALITY MONITORING ******************************")

print("\n")

print("CPCB - Indian Central Pollution Control Board")

print("Individual Air Quality")

print("City : ",city)

print("State : ",state)

print("Country : ",country)

print("Geographic Location : ",coordinates)

print("Time Standard : ",time_standard)

AQI(aqius)

switch(mainus)

print("Humidity : ",humidity)

print("Temperature : ",temp)

print("Precipitation : ",precipitation)

print("Wind Speed : ",wind_speed)

print("Wind Direction : ",wind_direction)

 
