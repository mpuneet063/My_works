password = 'getyourgoals'
def passwordcheck():
    #checking if passwordletters and given_password_letters are identical
    while (1):
        entered_password = input("Enter password: ")
        if entered_password == password:
            print("password is correct")
            print("Access granted.")
            break
        else:
            print("Incorrect password")
            print("access denied")
            print("try again")

#driver code
passwordcheck()