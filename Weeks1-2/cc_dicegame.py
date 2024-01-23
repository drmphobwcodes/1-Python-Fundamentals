import random

high_score = 0


def dice_game():
    print("Current High Score: " + str(high_score))
    print("1) Roll Dice")
    print("2) Leave Game")
    choice = input("Enter your choice: ")
    if choice == "1":
        roll_dice()
    elif choice == "2":
        exit()
    else:
        print("Invalid input. Please try again.")
        dice_game()

def roll_dice():
    global high_score
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    print("You rolled a " + str(die1) + " and a " + str(die2) + ".")

    if total > high_score:
        print("You have a new high score!")
        high_score = total

    print("Your total score is " + str(total) + ".")

    


dice_game()
