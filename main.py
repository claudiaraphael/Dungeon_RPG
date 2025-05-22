print("Welcome to the RPG Dungeon!")
print("You are about to embark on an epic adventure.")
print("You will face many challenges and make important decisions.")
print("Prepare yourself, brave hero!") 

class Character:
    def __init__(self, armor=None, weapon=None, shield=None, health=100, stamina=100):
        self.armor = armor if armor is not None else {}
        self.weapon = weapon if weapon is not None else {}
        self.shield = shield if shield is not None else {}
        self.health = health
        self.stamina = stamina
        self.level = 1
        self.experience = 0

    def equip_armor(self, armor):
        armor = {}
        if armor = self.armor:
            print("You already have this armor equipped.")
        else:
            self.armor = armor
            print(f"You have equipped {armor} armor.")
        
    def gain_exp(self):
        self.experience += 20
        if self.experience >= 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.experience = 0
        self.health += 20
        self.stamina += 20

play = input('Do you want to play? (yes/no) ').lower().strip()

if play == "yes":
    hero = Character()

    print("Let's venture into the dungeon. Let's see how far you can go!")

    answer = input('You reach crossroads. Do you wish to go left or right? ').lower().strip()
    
    if answer == 'left':
        print('On this path, you start walking in the woods and you hear a creaking noise.')
    elif answer == 'right':
        print('You find a cabin in the midst of the rain just before the entrance to a cave.')
        choice1 = input('Do you go into the cabin or enter the cave? a/b ').lower().strip()

        if choice1 == 'a':
            choice2 = input('You enter the cabin and find a treasure chest and some armory. Equip? y/n ').lower().strip()
            if choice2 == 'y':
                print("You have now equipped yourself with a sword and a shield.")
                hero.equip_armor("sword", 3)
                hero.equip_armor("shield", 2)
                print("You are now ready to face the challenges ahead.")
                hero.experience += 20
                print("You have gained 20 experience points.")
                hero.gain_exp()
                print("You have gained 20 experience points.")


else:
    print('See you next time!')
    quit()