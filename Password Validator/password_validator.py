'''Must contain at least 8 characters;
Must contain at least one uppercase letter;
Must contain at least one lowercase letter;
Must contain at least one number;
Must contain at least one special character any of ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+']
Should not contain spaces'''

def password_checker(password):

    special_char = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+']
    
    if len(password) < 8:
        print("Password must contain at least 8 characters.")
        return False

    if not any(char.isupper() for char in password):
        print('Password must contain at least one uppercase letter.')
        return False

    if not any(char.islower() for char in password):
        print('Password must contain at least one lowercase letter.')
        return False

    if not any(char.isdigit() for char in password):
        print('Password must contain at least one number.')
        return False
    
    if not any(char in special_char for char in password):
        print("Password must contain at least one special characters.")
        print("Special Characters :  " + "  ".join(special_char) )
        return False
    
    if any(char.isspace() for char in password):
        print('Password should not contain spaces.')
        return False

    print("Your Password is valid.")
    return True




pwd = input('Enter the password: ')
print(password_checker(pwd))