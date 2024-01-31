class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def change_password(self, password):
        self.password = password
        print("Ypur password has been changed to", password)

class BankUser(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.balance = 0

    def check_balance(self):
        print("Your balance is $100")

bankuser1 = BankUser("Jane", "jane@nucamp.co", "bestpassword")


