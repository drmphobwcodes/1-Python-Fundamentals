from banking_pkg import account


def atm_menu(name):
    #print("Welcome: " + name)
    print("          === Automated Teller Machine ===          ")
     # Registration loop with PIN validation
    while True:
        # Prompt user to enter name
        name = input("Enter name to register: ")

        # Check if the length of the name is between 1 and 10 characters
        if 1 <= len(name) <= 10:
            break  # Exit the loop if the name is valid
        else:
            print("Invalid name! Please enter a name with a length between 1 and 10 characters.")

    # PIN validation loop
    while True:
        # Prompt user to enter PIN
        pin = input("Enter PIN: ")

        # Check if the length of the PIN is 4 characters
        if len(pin) == 4:
            break  # Exit the loop if the PIN is valid
        else:
            print("Invalid PIN! Please enter a 4-digit PIN.")

    # Declare and initialize balance variable
    balance = 0
    print(name +  " has been registered with a starting balance of $" + str(balance))

    print("          === Automated Teller Machine ===          ")
    print("LOGIN")
    while True:
        #request user name and pin for login
        name_to_validate = input("Enter name: ")
        pin_to_validate = input("Enter PIN: ")
        #validate user name and pin entered match the registered user name and pin
        if name_to_validate == name and pin_to_validate == pin:
            print("Login successful for " + name)
            break
        else:
            print("Invalid credentials")

    print("          === Automated Teller Machine ===          ")
    while True:
        print("User: " + name)
        print("------------------------------------------")
        print("| 1.    Balance     | 2.    Deposit      |")
        print("------------------------------------------")
        print("------------------------------------------")
        print("| 3.    Withdraw    | 4.    Logout       |")
        print("------------------------------------------")
        option = input("Choose an option: ")
        #Check if user has selected option 1, 2, 3 or 4
        if option == "1":
            #Call show_balance function from account.py
            account.show_balance(balance)
        elif option == "2":
            #Call deposit function from account.py
            balance = account.deposit(balance)
            #Displayingt the updated amount
            account.show_balance(balance)
            
        elif option == "3":
            #Call withdraw function from account.py
            balance = account.withdraw(balance)
            #Displayingt the updated amount
            account.show_balance(balance)
            
        elif option == "4":
            #Call logout function from account.py
            account.logout(name)
        
            break
        else:
            print("Invalid option selected")

atm_menu("JWells Fargo")

