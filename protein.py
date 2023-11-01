import os

def common_proteins():
    while(True):
        os.system('clear') 
        print("Here is a list of common protein meats used.")
        print("1. Beef\n2. Pork\n3. Chicken\n4. Fish\n5. Turkey\n6. Lamb\n7. Shrimp\n8. Veal\n9. Duck\n10. Bison")
        print("Enter Q to return to the main menu.")
        print("FYI: A new feature is to instead enter the number of the protein to learn more.\nThis will show you a paragraph about some information about the protein.")
        user_input = get_input()
        if(user_input == 'Q'):
            os.system('clear')  
            return
        else:
            extra_info(user_input)

def extra_info(user_input):
    os.system('clear') 
    if(user_input == 1):
        print("1")
    elif(user_input == 2):
        print("2")
    elif(user_input == 3):
        print("3")
    elif(user_input == 4):
        print("4")
    elif(user_input == 5):
        print("5")
    elif(user_input == 6):
        print("6")
    elif(user_input == 7):
        print("7")
    elif(user_input == 8):
        print("8")
    elif(user_input == 9):
        print("9")
    elif(user_input == 10):
        print("10")
    user_input = input("Once your done reading enter 'Q' to go back to the list here-->:")
    while(True):
        if(user_input != 'Q'):
            user_input = input("Please enter Q to quit:")
        else:
            return



def get_input():
    valid = False
    while(valid == False):
        user_input = input("Type choice here-->:")
        if(user_input == 'Q'):
            return 'Q'
        
        if(user_input.isdigit()):
            int_version = int(user_input)
            if(int_version >=1 and int_version<= 5):
                valid = True
                return int_version
        os.system('clear')  
        print("Sorry that number wasn't on the list please try again.")
        valid = False
