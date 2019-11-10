


# flag for loop
active = True

name = input("Please enter your name: ")
password = input("Enter your password: ")

print(check_if_pass_isn_db())


print("Hi {} Logged in".format(name))

def save_password():
    '''creates and stores a password'''
    with open(filename, 'w') as f_obj:
        f_obj.write(password)


def check_if_pass_isn_db():
    '''Checks if the password is in db'''
    filename = 'passwords.txt'
    with open(filename) as f_obj:
        contents = f_obj.read()
    if contents != password:
        print('Please store a password')
        save_password()



