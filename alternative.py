import os

def alternatives():
    print("Welcome to alternative options. Here are 10 common alternatives to common meat proteins.")
    print("1. Legumes\n2. Tofu/Tempeh\n3. Seitan\n4. Quinoa\n5. Nuts/Seeds\n6. Edamame\n7. Spirulina\n8. Mycoprotein\n9. Vegitables\n10. Nutritional Yeast")
    user_input = get_input()
    if(user_input == 'Q'):
        os.system('clear')  
        return


def get_input():
    valid = False
    while(valid == False):
        user_input = input("Enter Q to quit and return to main menu here-->:")
        if(user_input == 'Q'):
            return 'Q'
        print("Please enter Q to quit")
        
