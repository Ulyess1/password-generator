import random
import string
import csv
from pathlib import Path
FILE = Path(__file__).parent / "save.csv"

def upper():
  return string.ascii_uppercase
def lower() :
  return string.ascii_lowercase
def digits() :
  return string.digits
def special() :
  return string.punctuation

print("1-upper letters.")
print("2-lower letters.")
print("3-Numbers.")
print("4-Special charahcters.")
print("0-Exit")
choice = input("Select Your Choice : ")
if choice == "1" :
  value = upper()
elif choice == "2" :
  value = lower()
elif choice == "3" :
 value = digits()
elif choice == "4" :
 value = special()
elif choice == "0":
  print("Good Bye..")
  value = None 
  
if value is not None :
 print(value)
 with open(FILE, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([value,])