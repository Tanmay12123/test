
light_state = False

while 1==1:
   
    user_value = input("value:  ")
    if user_value == "ON" or user_value=="on":
        print("Turning on the light")
        light_state =True
        # pass
        #if light_state == True:
            #print("Light is aldready switched on") 
    elif user_value == "OFF" or   user_value == "off":
        print("Turning off the light")
        light_state = False
        #if light_state == False:
        # print("Light is aldready switched off")
    else:
        print("Sorry, that was an invalid command!")
        pass
        
        
    # for i in range(10):
    print("The current state of the light is:", light_state)
        # user_input()