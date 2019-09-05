import getpass
print "Coded by George Bakalis"
print ("Login System")
Correct_Username = "Your_username"
Correct_Password = "Your_password"
 
loop = 'true'
while (loop == 'true'):
    username = raw_input("Enter your username: ")
    if (username == Correct_Username):
        password = getpass.getpass("Enter password for user %s: " % Swsto_Username)
        if (password == Correct_Password):
            print "Successful login as " + username
            loop = 'false'
        else:
            print "Wrong Password!"
    else:
        print "Wrong Username!"
