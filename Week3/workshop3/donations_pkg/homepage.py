'''
Homepage functions
'''


def show_homepage(authorized_user):
    '''
    show_homepage
        # TODO: Homepage menu view
    '''

    print("    === DonateMe Homepage ===             ") 
    print("------------------------------------------")
    print("| 1.    Login     | 2.    Register       |")
    print("------------------------------------------")
    print("| 3.   Donate   | 4.    Show Donations   |")
    print("------------------------------------------")
    print("|           5.       Exit                |")
    print("------------------------------------------")

    
   


def donate(username):
    '''
    donate
        # TODO: Donation action
    '''
    donation_atm = float(input("Enter amount to donate"))
    donation_string = "{} donated ${}".format(username, donation_atm)
    print("Thank you for your donation, {}!".format(username))
    return donation_string
    


def show_donations(donations):
    '''
    show_definition
        # TODO: show donations view
    '''
    print("\n---All donations---")
    if donations == []:
        print("Currently, there are no donations.")
    else:
        for donation in donations:
            print(donation)


