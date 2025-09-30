import random
import string
import csv
from pathlib import Path
FILE = Pat(__file__).parent / ""
def upper(min_length):
 upper_letters = string.ascii_uppercase 
 print(upper_letters)
def lower(min_length) :
 lower_letters = string.ascii_lowercase
 print(lower_letters)
def digits(min_length) :
 Numbers = string.digits
 print(Numbers)
def punctuation(min_length) :
 special = string.punctuation
 print(special)

print("1-upper letters.")
print("2-lower letters.")
print("3-Numbers.")
print("4-Special charahcters.")
choice = input("Select Your Choice : ")
if choice == "1" :
 upper(1)
if choice == "2" :
 lower(1)
if choice == "3" :
 digits(1)
if choice == "4" :
 punctuation(1)