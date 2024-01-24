import random

diamonds = ['AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'KD', 'QD']
hand = []

while diamonds:
    user = input("Press enter to pick a card, or Q then enter to quit: ")   
    if user.lower() == 'q':
        break
    else:
        card = random.choice(diamonds)
        hand.append(card)
        diamonds.remove(card)
        print("Your hand: ", hand)
        print("Remaining cards: ", diamonds)
        print()
print("Your final hand: ", hand)

if not diamonds:
    print("There are no more cards to pick.")