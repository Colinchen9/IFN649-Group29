import time
import paho.mqtt.publish as publish



import requests
import json

def readFromServer():
    url_items = "https://tianqiapi.com/api?version=v6&appid=85613835&appsecret=2lLW0QSO"
    prompt1 = 'analytic information'
    
    city = "HongKong"
    response = requests.get(url_items)
    payload = response.json()
    
    location = ["city"]
    update_time = payload['update_time']
    real_time_temperature = payload["tem"]
    #real_time_air = payload["air"]
    real_time_humidity = payload["humidity"]
    print("location: " + city)
    print("update_time: " + city)
    print("real_time_temperature: " + real_time_temperature)
    print("real_time_humidity: " + real_time_humidity)
    
    publish.single(topic="Temperature", payload='realtime-temperature is %s' % real_time_temperature, hostname="localhost")
    
    if int(real_time_temperature) > 20:
        prompt1 = 'high temperature alert, need to cool down'
        publish.single(topic="Temperature", payload='analytic information: %s' % prompt1, hostname="localhost")

    if int(real_time_humidity) < 50%:
        prompt2 = 'too dry need some water'
        publish.single(topic="Humidity", payload='analytic information: %s' % prompt2, hostname="localhost")
        
    time.sleep(6)
