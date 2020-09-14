#install and import 
#libraries
import requests
from pynotifier import Notification

url = "http://api.openweathermap.org/data/2.5/weather?q="
#enter your city
cityname = ""
#enter your api key
api_key = ''

data = requests.get(url+cityname+'&appid='+api_key).json()

#define
city = data['name']
country = data['sys']['country']
temperature = data['main']['temp_max'] -273.15
weather = data['weather'][0]['main']
wind_speed = float (data['wind']['speed'])
humidity = data['main']['humidity']
pressure = data['main']['pressure']

if data["cod"] != "404":
    Notification(
        title = city+","+country,
        description = f'{temperature},°C {weather}\n Wind Speed {wind_speed}\n Humidity {humidity}\n Pressure {pressure}',
        duration= 100,
        urgency= Notification.URGENCY_CRITICAL).send()

else:
    print("City Not Found !!")