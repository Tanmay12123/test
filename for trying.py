light_state=True

user_value=""
# while 1==1:

def checker():
    if user_value == "ON" or user_value=="on":
        print("Turning on the light")
        light_state =True
        print("Samosa")
        # pass
        #if light_state == True:
            #print("Light is aldready switched on") 
    elif user_value == "OFF" or   user_value == "off":
        print("Turning off the light")
        light_state = False
        print("samosa false")
        #if light_state == False:
        # print("Light is aldready switched off")
    else:
        print("Sorry, that was an invalid command!")
        # pass
    return light_state
        
for i in range(10):
    user_value = input("value:  ")
    print("The current state of the light is:", checker())
    # user_input()