import datetime
import os
import work_weather


# show current date and time
def ask_date():
    print(datetime.datetime.now())
    

def weather():
    city_weather = work_weather.current_weather()
    print('Nhiet do hien tai o', city_weather[1], 'la', city_weather[0], 'do C')
    

# switch between functions


while True:
    user_input = input("How can I help? ")
    
    if user_input == "What time is this?":
        ask_date()
    elif user_input == "How is the weather?":
        weather()
    elif user_input == "Goodbye":
        print("Bye!")
        break
    else:
        print("Sorry, I don't understand.")
    
     
