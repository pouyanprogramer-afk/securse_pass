import string
import secrets
from validator import validator



def generat_pass():
    characters, snake_case = validator()  
    
    password = ''.join(secrets.choice(characters) for i in range(snake_case)) 
    
    return password

