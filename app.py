import string
import random 
def password_generator(min_length, numbers=True, special=True):
    
    letters = string.ascii_letters
    digits = string.digits
    punct = string.punctuation

    pool = letters
    if numbers :
        pool += digits
    if special :
        pool += punct

    pwd = ""
    has_number = True
    has_special = True

    while (not has_number if numbers else False) or (not has_special if special else False) or len(pwd) < min_length :
        new_char = random.choice(pool)
        pwd += new_char
        if new_char in digits :
            has_number = True
        elif new_char in punct :
            has_special = True

    return pwd 
min_length = int(input("enter the minimum length of password you want to generate :")) 
has_number = input("do you want to have numbers in your password y/n ? :").lower == "y" 
has_special = input("do you want to have special characters in your password y/n ? :").lower == "y"
pwd = password_generator(min_length,has_number,has_special)
print("your password is : ",pwd)