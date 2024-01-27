'''
User functions
'''


def login(database, username, password):
    '''
    login
        # TODO: Login action
    '''
    username = username.lower()
    if username in database and database[username] == password:
        print("Welcome, , {}!".format(username))
        return username
    elif username in database and database[username] != password:
        print("Incorrect password for {}".format(username))
        return ""
    else:
        print("Username not found.Please register")
        return ""


def register(database, username):
    '''
    register
        # TODO: Register user action
    '''
    username = username.lower()
    if username in database:
        print("Username already exists")
    else:
        password = input("Please enter a password: ")
        database[username] = password
        print("Username '{}' has been registered." .format(username))
        return database
    
