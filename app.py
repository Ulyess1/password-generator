import string
import csv
import random
from pathlib import Path

def csv_library(pwd):
    save_file = Path.cwd() / "save.csv"
    with save_file.open("a",newline="" ,encoding= "utf-8") as f :
     writer = csv.writer(f)
     writer.writerow([pwd])
    print("")
    print("Saved password to ",save_file)

def password_generator(min_length,numbers = True,special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
 
    characters = letters
    if numbers:
        characters += digits
    if special:
        characters += special
    
    pwd = ""
    meets_criteria = False
    has_number = False
    has_special= False

    while not meets_criteria or len(pwd) < min_length :
        new_char = random.choice(characters) 
        pwd += new_char

        if new_char in digits:
            has_number = True 
        if new_char in special :
            has_special = True
        
        meets_criteria = True
        if numbers :
            meets_criteria = has_number
        if special_characters :
            meets_criteria = meets_criteria and has_special

    return pwd
min_length = int(input("Enter length of your password to be generated : "))
has_number = input("Do you want numbers in your password ? y/n : ").lower() == "y"
print("")
has_special = input("Do you want special characters in your password ? y/n : ").lower() == "y"
print("")
pwd = password_generator(min_length , has_number , has_special)
print("Here is your generated password : " ,pwd)
print("")
print("Do You want to save password to a file ?.")
print("1-Yes.")
print("2-No.")
choice = input(" 1 / 2 :  ").strip()
if choice == "1":  
        csv_library(pwd)
elif choice == "2":
        print("Good Bye..")
else:
        print("Good Bye..")