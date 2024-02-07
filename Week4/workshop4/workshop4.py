"""
Week 4 workshop 
By: Mpho Musengua
Version 1.3
Last Updated: 02/03/2024
"""
# used to type hint BankUser within Bankuser in Python 3.7+
from __future__ import annotations
import sys

# ---------- Task One ----------
# - Declare a class and give it the name "User"
# - The __init__ method has parameters defined as (self, name, pin, password)
# - The attribute of the User class are defined as (name, pin, and password)

# NOTE: Please properly impliment DocStrings!


class User:
    """
    User Class
    """

    def __init__(self, name: str, pin: int, password: str):
        """
        Initialize
        """
        self.name = name
        self.pin = pin
        self.password = password
        # ---------- Task Two ----------
        # The "User" class should have three methods:
        #    * change_name - changes the name of User
        #    * change_pin - changes the PIN code of User
        #    * change_password - changes the password of User

    def change_name(self, new_name: str):
        """
        change_name
        """
        self.name = new_name


    def change_pin(self, new_pin: int):
        """
        change_pin
        """
        self.pin = new_pin

    def change_password(self, new_pw: str):
        """
        change_password
        """
        self.password = new_pw


class BankUser(User):

    """
    ---------- Task Three ----------
        - Declare a class and give it the name "BankUser"
        - "BankUser" class will inherit the "User" class
        - The __init__ method has parameters defined as (self, name, pin, password)
        - The super method has parameters defined as (name, pin, password)
        - The attributes of the "BankUser" is balance with a default value of zero.
    """
    

    # ----------Task Four ----------
    # The "BankUser" class should have three methods:
    #    * show_balance- prints the balance of the User
    #    * withdraw - withdrawing money decreases the account balance
    #    * deposit - depositing money increases the account balance
    def __init__(self, name: str, pin: int, password: str):
        """Initialize"""
        # TODO: Initialize and call super()
        self.name = name
        self.pin = pin
        self.password = password
        self.balance = 0 # default value of zero

    def show_balance(self):
        """
        show_balance
        """
        print(f"{self.name} has an account balance of: {self.balance}")

    def withdraw(self, amount: int):
        """
        withdraw
        """
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount


    def deposit(self, amount: int):
        """
        deposit
        """
        self.balance += amount

    def transfer_money(self, user: BankUser, amount: int) -> bool:
        """
        transfer_money
        """
        
        # ----------Task Five ----------
        # Create more methods for the BankUser class:
        #    * transfer_money
        #        - Transfers money to another User if
        #        - correct PIN is given for transferring User

        print(f"You are transferring ${amount} to {user.name}")
        print("Authentication required")
        user_pin = int(input("Enter your PIN: "))
        if user_pin == self.pin:
            print("Transfer authorized")
            self.withdraw(amount)
            user.deposit(amount)
            print(f"Transferring ${amount} to {user.name}")
            print(f"{user.name} has an account balance of: {user.balance}")
            print(f"{self.name} has an account balance of: {self.balance}")
            return True
        else:
            print("Invalid PIN. Transfer not authorized")
            print(f"{self.name} has an account balance of: {self.balance}")
            return False

        
        



        
       
    def request_money(self, user: BankUser, amount: int) -> bool:
        """
        request_money
        """
        # ----------Task Five ----------
        # Create more methods for the BankUser class:
        # * request_money
        #    - Will ask for the PIN of the User being requested for money.
        #    - If credentials are correct:
        #        - Will ask for and validate the password of the User requesting money,
        #        - Then complete the transfer, removing money from one account
        #            and adding the same amount to the other.
        print(f"You are requesting ${amount} from {user.name}")
        print("User authentication is required...")
        user_pin = int(input("Enter Bob's PIN: "))
        if user_pin == user.pin:
            user_pw = input("Enter your password: ")
            if user_pw == self.password:
                print("Request authorized")
                user.withdraw(amount)
                self.deposit(amount)
                print(f"{user.name} sent ${amount}")
                print(f"{self.name} has an account balance of: {self.balance}")
                print(f"{user.name} has an account balance of: {user.balance}")
                return True
            else:
                print("Invalid password. Transfer not authorized")
                print(f"{self.name} has an account balance of: {self.balance}")
                print(f"{user.name} has an account balance of: {user.balance}")
                return False
        else:
            print("Invalid PIN. Request not authorized")
            print(f"{self.name} has an account balance of: {self.balance}")
            print(f"{user.name} has an account balance of: {user.balance}")
            return False


# # # Driver Code for Task One
# # # Output: Bob 1234 password
        
#user1 = BankUser("Bob", 1234, "password")
#print(user1.name, user1.pin, user1.password)

# # # Driver Code for Task Two
# # # Output: Bob 1234 password
# # # Output: Bobby 4321 newpassword

#user1 = BankUser("Bob", 1234, "password")
#print(user1.name, user1.pin, user1.password)
#user1.change_name("Bobby")
#user1.change_pin(4321)
#user1.change_password("newpassword")
#print(user1.name, user1.pin, user1.password)


# # # Driver Code for Task Three
# # # Output: Bob 1234 password 0

#bankuser1 = BankUser("Bob", 1234, "password")
#print(bankuser1.name, bankuser1.pin, bankuser1.password, bankuser1.balance)


# # # Driver Code for Task Four
# # # Output:
# # #   Alice has an account balance of: 0
# # #   Alice has an account balance of: 1000.0
# # #   Alice has an account balance of: 500.0

#bankuser1 = BankUser("Alice", 1234, "password")
#bankuser1.show_balance()
#bankuser1.deposit(1000.0)
#bankuser1.show_balance()
#bankuser1.withdraw(500.0)
#bankuser1.show_balance()


# # # Driver Code for Task Five
# # # Output:
# # #   Alice has an account balance of: 5000
# # #   Bob has an account balance of: 0

# # #   You are transferring $500 to Bob
# # #   Authentication required
# # #   Enter your PIN: 5678
# # #   Transfer authorized
# # #   Transferring $500 to Bob
# # #   Alice has an account balance of: 4500
# # #   Bob has an account balance of: 500

# # #   You are requesting $250 from Bob
# # #   User authentication is required...
# # #   Enter Bob's PIN: 1234
# # #   Enter your password: alicepassword
# # #   Request authorized
# # #   Bob sent $250
# # #   Alice has an account balance of: 4750
# # #   Bob has an account balance of: 250


bankuser1 = BankUser("Bob", 1234, "password")
bankuser2 = BankUser("Alice", 5678, "alicepassword")
bankuser2.deposit(5000)


#showing initial balance
bankuser2.show_balance()
bankuser1.show_balance()
print()

transferred = bankuser2.transfer_money(bankuser1, 500)
bankuser1.show_balance()
print()

# if transferred:
bankuser2.request_money(bankuser1, 250)

#if not transferred:
if not transferred:
    sys.exit()

