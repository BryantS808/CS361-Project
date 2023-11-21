import os
import time

def converter():
    print("Welcome to the weight converter, this will convert 3 common units of weight to each other.Grams, ounces and pounds. Please use whole numbers.")
    print("Please select the current unit or if you want to exit enter 'Q'.")
    print("     1.Grams, g\n     2.Ounces, oz\n     3.Pounds, lbs")
    print("FYI: A new way to use the converter is to instead of going through each step just enter each value in one line.")
    print("    I.e:initial unit,final unit, amount. 12100 = convert 100 grams to ounces")
    starting = get_first_unit()
    if(starting == 'Q'):
        os.system('clear')
        return
    elif(starting > 3):
        print("One line input")
        print("call microservice with one line")
        call_microservice(str(starting))
        return
    final = get_second_unit(starting)
    amount = get_amount()
    final_string = str(starting) + str(final) + str(amount)
    print("Call micro service with final string: ", final_string)
    call_microservice(final_string)
    return
   

def call_microservice(input_string):
    with open("inputService.txt", 'w') as file:
        file.write(input_string)
    output = ''
    while(output == ''):
        with open("outputService.txt", 'r') as file:
            output = file.read()
    print("Conversion = ", output, "\n")
    with open("inputService.txt", 'w') as file:
        file.write('')
    return

def get_first_unit(): 
    valid = False
    while(valid == False):
        user_input = input("Please enter your number choice or 'Q' to quit here -->: ")
        if(user_input == 'Q'):
            return 'Q'
       
        #check if number is 1-3 or check validty of one line input
        if(user_input.isdigit()):
            int_version = int(user_input)

            #if one digit aka checking if the actual munerical value is 1-3
            if(int_version >=1 and int_version<= 3):
                valid = True
                return int_version
            #if the len is 3 or more its a possible attempt at one line input
            elif(len(user_input) >=3):
                #check that index 0 is 1-3, check if index 1 is 1-3, but not the same as index 0, and that the amount is greater than 0.
                if(int(user_input[0]) >= 1 and int(user_input[0]) <= 3):
                    if(int(user_input[1]) >= 1 and int(user_input[1]) <= 3 and int(user_input[0]) != int(user_input[1])):
                        if(int(user_input[2]) >  0):
                            valid = True
                            return int_version
                        else:
                            print("If you are trying to do a one line input your 3rd digit onward needs to be greater than 0")
                    else:
                        print("If you are trying to do a one line input your 2nd digit is either not 1-3 or you inputed the same option.")
                else:
                    print("If you are trying to do a one line input your first digit isn't one of the 3 options.")

                
        print("Sorry that number wasn't on the list please try again.")
        valid = False

def get_second_unit(start_unit):
    print("Please select a unit to convert to.")
    options = ["     1.Grams, g","     2.Ounces, oz","     3.Pounds, lb"]
    for i in  range(len(options)):
        if(i != start_unit -1):
            print(options[i])
    user_input = input("Please enter second unit here-->: ")
    while(True):
        if(user_input.isdigit()):
                int_version = int(user_input)
                #if one input
                if(int_version >=1 and int_version<= 3):
                    if(int_version != start_unit):
                        return int_version
                    else:
                        print("You have selected the same unit you wanted to convert from, please select a different unit.")
                else:
                    print("Please enter one of the choices 1 - 3, excluding the unit you want to convert from.")
        else:
            print("Please enter a valid number.")
        user_input = input("Enter choice here-->: ")
        
    
def get_amount():
    user_input = input("Enter the amount to be converted as a whole number here-->: ")
    while(True):
        if(user_input.isdigit() and int(user_input) >= 1):
            return int(user_input)
        user_input = input("Please input a valid number amount greater than zero as a whole number here-->: ")




    


