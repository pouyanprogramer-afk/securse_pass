import string
import secrets

def generat_pass():
    
    Characters = "" 
    
    try:
        snake_case = int(input("Enter the number of characters : (1/10) "))
        
        lowercaseـletters = input("Should I use lowercase letters ? (y/n) ") 
        
        if lowercaseـletters == "y":
            Characters += string.ascii_lowercase
        
        uppercase_letters = input("Should I use uppercase letters ? (y/n) ")

        if uppercase_letters == "y":
           Characters += string.ascii_uppercase

        digits = input("Should I use digits ? (y/n)")

        if digits == "y":
           Characters += string.digits

        punctuation = input("Should I use punctuation ? (y/n)")

        if punctuation == "y":
           Characters += string.punctuation 

        password = ''.join(secrets.choice(Characters) for i in range(snake_case))
    
    except Exception as error:
        print(type(error).__name__, error)

    return password