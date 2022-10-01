import random
while(True):
 Temperature=random.randint(1,70)
 Humidity=random.randint(1,50)
 if 10<Temperature>20:
    print(f"Dont go out the temperature is :{Temperature}")
 elif 20<Temperature>30:
    print(f"Get ready to do your daily routine temperature is:{Temperature}")
 elif 30<Temperature>35 :
    print(f"temperature is {Temperature} dont go out")
 else:
    print("Ring the alarm continously ")
if 1<Humidity >15:
    print(f"Humidity value is {Humidity}")
elif 15<Humidity>30:
    print(f"Humidity value is {Humidity}")
