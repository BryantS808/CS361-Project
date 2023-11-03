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
        print("Beef is a significant source of protein, iron, zinc, and B vitamins. It contains essential nutrients for muscle growth and repair. However, some cuts may also contain higher amounts of saturated fats.")
    elif(user_input == 2):
        print("Pork is rich in protein and various vitamins and minerals. It provides thiamine, niacin, riboflavin, zinc, and potassium. Leaner cuts of pork offer a good protein-to-fat ratio.")
    elif(user_input == 3):
        print("Chicken is a lean source of protein, low in saturated fat, and a good source of vitamins and minerals such as niacin, selenium, and vitamin B6. The breast meat, in particular, is low in fat and calories.")
    elif(user_input == 4):
        print("Fish, especially fatty fish like salmon and tuna, are rich in high-quality protein and omega-3 fatty acids. These healthy fats promote heart health and offer an excellent protein source.")
    elif(user_input == 5):
        print("Similar to chicken, turkey is a lean protein source. It contains nutrients like niacin, vitamin B6, and zinc, with lower levels of saturated fat compared to some other meats.")
    elif(user_input == 6):
        print("Lamb is a good source of protein, zinc, and vitamin B12. It can have a higher fat content, depending on the cut, but also provides essential vitamins and minerals.")
    elif(user_input == 7):
        print(" Shrimp is a protein-rich, low-calorie seafood option. It's high in iodine, selenium, and astaxanthin, while being low in saturated fat.")
    elif(user_input == 8):
        print("Veal offers a protein source with various vitamins and minerals, including riboflavin, vitamin B12, zinc, and selenium. It's often lower in fat than beef.")
    elif(user_input == 9):
        print("Duck meat provides iron, selenium, zinc, and several B vitamins. It can have a higher fat content compared to some poultry but offers valuable nutrients.")
    elif(user_input == 10):
        print("Bison is a lean meat choice rich in protein, iron, zinc, and vitamin B12. It's often preferred for its lower fat content compared to beef.")
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
