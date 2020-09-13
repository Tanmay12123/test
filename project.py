

def calculator(first_number,operators,second_number):
    
    print("Hello welcome to MDs calculator\n Type the operators according to your needs")
    first_number = int(input("Enter the 1 number:  "))
    operators = input("Enter your operator:  ")
    second_number = int(input("Enter the 2 number: "))
    
    if operators == "+":
        print(first_number+second_number)
        
        
    elif operators == "-":
        print(first_number -second_number)
        
    elif operators == "*":
        print(first_number *second_number)
        
    elif operators == "/":
        print(first_number /second_number)
    
    else:
        print("Sorry, we don't understand this operator")
               
print("Thank you for using the calculator")
user_choice =input("Please enter y/n to play again or quit:   ")

if user_choice== "y":
    print("yes!!")

elif user_choice== "n":
    print("Goodbye!     Meet you again")
    break

else:
    print("sorry I don't understand'")
    
