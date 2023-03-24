import re

print("This is a Username Verification Program\n Please input specific Username to be verified:")

username = input(str)

def usernameFunction(user):

    if (len(user) < 4 or len(user) >= 25):
        {
            print ("Output: False - Your username is either too short or too long")
        }
       
    elif not user[0].isalpha():
        {
            print("Output: False - First Letter not alphabet")
        }
            
    elif not re.match('^[a-zA-Z0-9_]+$',user):
        {
            print("Output: False - Contains Characters away from letters,numbers or underscores")
        }

    elif user[-1].isalnum():
        {
            print("Output: True. Your Username has met all these conditions\n 1.The username is between 4 and 25 characters.\n 2.It must start with a letter.\n 3.It can only contain letters, numbers, and the underscore character.\n 4.It cannot end with an underscore character.")
        }
    else:
        {
            print("Output: False")
        }
             
    return user

usernameFunction (username)


