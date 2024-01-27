'''
Workshop 3 framework v1.1
By Mpho Musengua

# Follow allong with the written workshop instructions and
    use this application stub to impliment the functionality.

# Locations marked with TODO: are places that need implimentation.

# The pass command in a stub is used to end a block and continue execution.
    This is used to define portsion of code structure that are awaiting implimentation.
    You should remove pass when you impliment the functionality.
'''
# TODO: import package functions:
# EXAMPLE FORMAT: from package.file imprort function_name, (...)
from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register


# Global (Application) variable definitions
database = {
    # TODO: Default users dictionary
    "admin": "password123"
}
donations = []
authorized_user = ""

#call the show_homepage function from the homepage module
show_homepage(authorized_user)

# Main application loop
#check if the user is logged in

    # TODO: Show homepage
if authorized_user == "":
    print("You are not logged in.")
else:
    print("You are logged in as: ", authorized_user)

#Main program loop
while True:
    print("    === DonateMe Homepage ===             ")
    print("------------------------------------------")
    print("| 1.    Login     | 2.    Register       |")
    print("------------------------------------------")
    print("| 3.   Donate   | 4.    Show Donations   |")
    print("------------------------------------------")
    print("|           5.       Exit                |")
    print("------------------------------------------")
    option = input("Please select an option: ")

    if option == "1":  
        print ("\nLogin:")
        username = input("Username: ")
        password = input("Password: ")
        authorized_user = login(database, username, password)
    elif option == "2":
        print ("\nRegister:")
        username = input("Enter username: ")
        authorized_user = register(database, username)
    elif option == "3":
        print ("\nDonate:")
        if authorized_user == "":
            print("You are not logged in.")
        else:
            donations_result = donate(authorized_user)
            donations.append(donations_result)
    elif option == "4":
        show_donations(donations)
    elif option == "5":
        print ("Goodbye!")
        break
    else:
        print("Invalid option selected.")