#Declaring 3 variabels for the 3 characters in the game- Character names are strings

wizard = "Wizard"
elf = "Elf"
human = "Human"
dragon = "Dragon"
#Declaring 3 variables for the 3 characters' hit points (Characters' hit points are integers)
wizard_hp = 70
elf_hp = 100
human_hp = 150
#Declaring 3 variables for the 3 characters' damage(Characters' damage are integers)
wizard_damage = 150
elf_damage = 100
human_damage = 20
#Declaring two variables that set the hp and damage for the Dragon - 300 hp and 50 damage
dragon_hp = 300
dragon_damage = 50

# #Ptrompts the player to choose a character by showing them the 3 options
# print ("Choose your character:")
# print("1) " + wizard)
# print("2) " + elf)
# print("3) " + human)
# #Prompts the player to choose a character by entering the number that corresponds to the character
# character = input("Choose your character: ")
# #Check user's input
# if character == "1":
#     character = wizard
#     my_hp = wizard_hp
#     my_damage = wizard_damage
# elif character == "2":
#     character = elf
#     my_hp = elf_hp
#     my_damage = elf_damage
# elif character == "3":
#     character = human
#     my_hp = human_hp
#     my_damage = human_damage
# else:
#     print("Unknown Character")

#While loop that runs while the dragon's hp is greater than 0
while True:
    print("Choose your character:")
    print("1) Wizard")
    print("2) Elf")
    print("3) Human")
    character = input("Choose your character: ")

    #Check user's input
    if character == "1":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    elif character == "2":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    elif character == "3":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    else:
        print("Unknown Character")
#Prints the character that the player has chosen
print("You have chosen the character: " + character)

#Battle with the Dragon
while True:
    dragon_hp = dragon_hp - my_damage
    print("The", character, "damaged the Dragon!")
    print("The Dragon's hitpoints are now:", dragon_hp)
    if dragon_hp <= 0:
        print("The Dragon has lost the battle")
        break 
    my_hp = my_hp - dragon_damage
    print("The Dragon strikes back at", character)
    print("The", character, "'s hitpoints are now:", my_hp)
    if my_hp <= 0:
        print("The", character, "has lost the battle")
        break

