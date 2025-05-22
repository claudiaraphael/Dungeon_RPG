print("Welcome to the RPG Dungeon!")
print("You are about to embark on an epic adventure.")
print("You will face many challenges and make important decisions.")
print("Prepare yourself, brave hero!") 

# User selects if they want to play or quit
play = input('Do you want to play? (yes/no) ').lower().strip()


if play == "yes":
    print("Let's venture into the dungeon. Let's see how far you can go!")
else:
    print('See you next time!')
    quit()