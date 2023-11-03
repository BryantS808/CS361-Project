import os
import protein
import cal_track
import weight_convert
import alternative

def main():
    exit = False
    print("Welcome to whatever this is.\n")
    while(exit == False):
        user_input = get_input()
        if(user_input == 1):
            protein.common_proteins()
        elif(user_input == 2):
            cal_track.cal_track()
        elif(user_input == 3):
            weight_convert.converter()
        elif(user_input == 4):
            alternative.alternatives()
        else:
            confirm = quit()
            if(confirm == True):
                return


def get_input():
    valid = False
    while(valid == False):
        print("Main Menu")
        print("Please select a function by entering a number.")
        print("     1.List common meat protein sources.\n     2.Calorie Tracker\n     3.Weight Unit Conversion\n     4.Alternative Options\n     5.Exit ")
        user_input = input("Type number choice here-->:")
        if(user_input.isdigit()):
            int_version = int(user_input)
            if(int_version >=1 and int_version<= 5):
                valid = True
                return int_version
        os.system('clear')  
        print("Sorry that number wasn't on the list please try again.")
        valid = False
def quit():
    while(True):
        confirmation = input("Are you sure you want to Exit the app. If you are sure enter 'Y' if not enter 'N' here-->: ")
        if(confirmation == 'Y'):
            return True 
        elif(confirmation == 'N'):
            os.system('clear')
            return False
        else:
            print("Please enter Y or N to confirm.")



if __name__ == "__main__":
    main()