def show_balance(balance):
    print("Your current balance is: " + str(balance))
    

def deposit(balance):
    #Request amount to deposit into the account
    amount = float(input("Enter amount to deposit: "))
    return balance + amount
    

def withdraw(balance):
    #Request amount to withdraw from the account
    amount = float(input("Enter amount to withdraw: "))
    return balance - amount
    

def logout(name):
    print("Goodbye " + name)