import getpass
print "Coded by George Bakalis"
print ("Login System")
Swsto_Username = "Your_username"
Swsto_Password = "Your_password"
 
loop = 'true'
while (loop == 'true'):
    username = raw_input("Enter your username: ")
    if (username == Swsto_Username):
        password = getpass.getpass("Enter password for user %s: " % Swsto_Username)
        if (password == Swsto_Password):
            print "Successful login as " + username
            loop = 'false'
        else:
            print "Wrong Password!"
    else:
        print "Wrong Username!"
