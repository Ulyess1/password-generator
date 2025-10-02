🔐 Password Generator

A simple Python script to generate secure passwords with customizable options for length, numbers, and special characters. The generated password can optionally be saved into a save.csv file.

✨ Features

Generate random passwords with:

Uppercase and lowercase letters

Optional numbers

Optional special characters

Minimum length defined by the user

Ensures generated password meets criteria (contains at least one number or special character if requested)

Saves generated password to a CSV file (save.csv)

📂 Project Structure
password_generator.py   # Main script
save.csv                # File where passwords are saved (auto-created)

🛠 Requirements

Python 3.x

Standard libraries used:

string

csv

random

pathlib

(No external dependencies required.)

🚀 Usage

Clone or download this project.

Run the script:

python password_generator.py


Follow the prompts:

Enter minimum password length

Choose whether to include numbers (y/n)

Choose whether to include special characters (y/n)

Your password will be displayed and automatically saved to save.csv.

📋 Example
Enter length of your password to be generated : 12

Do you want numbers in your password ? y/n : y

Do you want special characters in your password ? y/n : y

Here is your generated password :  9dF&gT@z1!Lp

Saved password to  /your/path/save.csv

💡 Notes

If you don’t want to save the password, remove the last block of code that writes to save.csv.

Passwords are appended to the file each time the script is run.

🔮 Future Improvements

Option to name and store multiple passwords with labels (e.g., for accounts).

GUI-based password generator.

Option to copy password directly to clipboard.