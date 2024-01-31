class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def change_password(self, password):
        self.password = password

user1 = User("jane", "jane@nucamp.com", "janespassword")
print(user1.password)
user1.change_password("bestpassword")
