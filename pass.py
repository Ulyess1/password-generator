import csv
import random
from pathlib import Path

FILE = Path(__file__).parent / "passwords.csv"

def password(pwd_length=8, file_path=FILE):
    pwd = ''.join(chr(random.randint(32, 126)) for _ in range(pwd_length))
    print("password:", pwd)

    with open(file_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([pwd])

    return pwd

if __name__ == "__main__":
    password(10)
