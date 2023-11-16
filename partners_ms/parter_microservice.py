import random
import time


phrases = [
    "Break a leg!",
    "Piece of cake.",
    "The ball is in your court.",
    "Bite the bullet.",
    "A piece of the pie.",
    "The whole nine yards.",
    "Cost an arm and a leg.",
    "Hit the hay.",
    "Burn the midnight oil.",
    "Spill the beans.",
    "Jump on the bandwagon.",
    "The early bird catches the worm.",
    "Don't cry over spilled milk.",
    "Bite off more than you can chew.",
    "Grasping at straws."
]

while(True):
    with open("phrase.txt", 'r') as file:
        command = file.read()
    print("Read ", command)
    if(command == "run"):
        random_number = random.randint(1, 15)
        print(random_number)
        with open("phrase.txt", 'w') as file:
            file.write(phrases[random_number])
    else:
        print("Sleeping.")
        time.sleep(5)
    