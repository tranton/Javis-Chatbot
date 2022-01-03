import requests, json
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    # print(text)

def current_weather():
    
    city = input('Enter city name: ')

    ow_url = "http://api.openweathermap.org/data/2.5/weather?"
      
    if not city:
        pass
    api_key = "3f70815b7c3966a2f1ebd49f1fb1b41a"
    call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    response = requests.get(call_url)
    data = response.json()
    jprint(response.json())

    if data["cod"] != "404":
        city_res = data["main"]
        current_temperature = city_res["temp"]
        current_pressure = city_res["pressure"]
        current_humidity = city_res["humidity"]
        suntime = data["sys"]
        # sunrise = datetime.datetime.fromtimestamp(suntime["sunrise"])
        # sunset = datetime.datetime.fromtimestamp(suntime["sunset"])
        wthr = data["weather"]
        weather_description = wthr[0]["description"]
        # now = datetime.datetime.now()
        # print(current_temperature)
        
    else:
        print("Không tìm thấy địa chỉ của bạn")

    return current_temperature, city    


