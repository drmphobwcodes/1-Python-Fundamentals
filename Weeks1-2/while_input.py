while True:
    print("1. Number one")
    print("2. Number two")
    print("3. Break out of infinite loop")
    option = input("Choose your option: ")
    if option == "1":
        print("You chose option 1")
    elif option == "2":
        print("You chose option 2")
    elif option == "3":
        break
    else:
        print("Invalid option")
print("Goodbye!")