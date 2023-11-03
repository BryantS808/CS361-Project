import os


def cal_track():
    os.system('clear')
    print("Welcome to the calorie tracker!")
    print("You can use track for however long you want. One method is to track for the day and then clear the data for the next.")
    while(True):
        print("Here is your current tracking:")
        print_file_and_cals()
        print("")
        user_input = get_input()
        if(user_input == 4):
            os.system('clear')
            return
        elif(user_input == 1):
            os.system('clear')
            add()
        elif(user_input == 2):
            os.system('clear')
            edit()
        else:
            clear()
def clear():
    while(True):
        confirmation = input("Are you sure you want to clear. Are you done tracking for this period of time? If you are sure enter 'Y' if not enter 'N' here-->: ")
        if(confirmation == 'Y'):
            with open('cal_store.txt', 'w') as file:
                file.truncate(0)
            os.system('clear')
            return
        elif(confirmation == 'N'):
            os.system('clear')
            return
        else:
            confirmation = input("Please enter 'Y' or 'N' capitalized to confirm clearing here-->: ")

def edit():
    print_file_and_cals()
    total_lines = 0
    with open('cal_store.txt', 'r') as file:
        total_lines = sum(1 for line in file)
    valid = False
    
    #Get line number
    line_number = 0
    while(valid == False):
        user_input = input("What line number would you like to edit? If you didn't mean to edit enter 'Q'. Enter here -->: ")
        if(user_input == 'Q'):
            os.system('clear')
            return
        elif(user_input.isdigit() == False or (int(user_input ) < 1 or int(user_input) > total_lines)):
            print("Please enter a valid line number")
        else:
            line_number = int(user_input)
            valid = True
    
    
    with open('cal_store.txt', 'r') as file:
        lines = file.readlines()

    food_name = input("What is the food or drink you are adding? Enter here -->: ")
    valid = False
    cals = ''
    # get calories and check its an int
    while(valid == False):
        temp = input("What are the calories of the item? Enter here -->: ")
        if(temp.isdigit() == False):
            print("Please enter a valid number.")
        else:
            cals = temp
            valid = True
    
    string = str(line_number) + ": " +food_name + ", " + cals + " cals\n"
    lines[line_number- 1] = string

    with open('cal_store.txt', 'w') as file:
            file.writelines(lines)
    
    


def add():
    print_file_and_cals()
    print("FYI: If you make a mistake here you can always edit it later.")
    food_name = input("What is the food or drink you are adding? If you did not mean to add enter 'Q to quit. Enter here -->: ")
    if(food_name == 'Q'):
        os.system('clear')
        return
    

    valid = False
    cals = ''
    # get calories and check its an int
    while(valid == False):
        temp = input("What are the calories of the item you just entered? Enter here -->: ")
        if(temp.isdigit() == False):
            print("Please enter a valid number.")
        else:
            cals = temp
            valid = True

    #make the line indexing
    total_lines = 0
    with open('cal_store.txt', 'r') as file:
        total_lines = sum(1 for line in file)
    total_lines += 1 
    line_number = str(total_lines) + ": "


    string = line_number + food_name + ", " + cals + " cals\n"
    with open('cal_store.txt', 'a') as file:
            file.write(string)
    
    
    os.system('clear')
    return


def print_file_and_cals():
    with open('cal_store.txt', 'r') as file:
        content = file.read()  # Reads the entire file
        print(content)
        file.seek(0)  # Reset file pointer to the start
        lines = file.readlines()
        total_cals = 0
        #Food, X cals
        for line in lines:
           calorie_string = line.split(',')[1]
           calories = (calorie_string.split("cals")[0]).strip()
           total_cals += int(calories)
        print("Total cals so far = ", total_cals)

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

def get_input():
    valid = False
    while(valid == False):
        print("Please select a function by entering a number.")
        print("     1.Add an item.\n     2.Edit a entry\n     3.Clear\n     4.Exit")
        user_input = input("Type number choice here-->:")
        if(user_input.isdigit()):
            int_version = int(user_input)
            if(int_version >=1 and int_version<= 4):
                valid = True
                return int_version
        os.system('clear')  
        print("Sorry that number wasn't on the list please try again.")
        valid = False

#cal_track()