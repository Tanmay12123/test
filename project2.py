user_value = input("value:  ")
light_state = False


if user_value == "ON"or "on":
    if light_state == True:
        print("Light is aldready switched on")
    print("Turning on the light")
    light_state =True
         
elif user_value == "OFF"or "of":
    print("Turning off the light")
    light_state =False
    if light_state == False:
        print("Light is aldready switched off")
    
for i in range(1):
    print(light_state)
    
