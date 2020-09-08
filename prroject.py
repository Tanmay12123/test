try:   
    x = int(input("Age:  "))
    if x > 100: 
        print("Put your real age not the fake one...")
    print(x)
except ValueError:
    print("I think the age only contains numbers why are you entering strings?")
    