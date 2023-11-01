import os
import protein
import cal_track



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
            pass
        elif(user_input == 3):
            pass
        else:
            exit = True

def get_input():
    valid = False
    while(valid == False):
        print("Please select a function by entering a number.")
        print("     1.List common meat protein sources.\n     2.Soemthing\n     3.Exit\n")
        user_input = input("Type number choice here-->:")
        if(user_input.isdigit()):
            int_version = int(user_input)
            if(int_version >=1 and int_version<= 5):
                valid = True
                return int_version
        os.system('clear')  
        print("Sorry that number wasn't on the list please try again.")
        valid = False

if __name__ == "__main__":
    main()