# Password Generator

Simple CLI password generator script that:
- Creates a random password using letters, optional numbers and special characters.
- Shows the generated password and whether it contains numbers / special chars.
- Optionally appends the password to `save.csv` in the current working directory (uses pathlib.Path).

## Requirements
- Python 3.6+
- No external packages (uses stdlib: string, random, csv, pathlib)

## Files
- `app.py` — main script containing:
  - `password_generator(min_length, numbers=True, special_characters=True)` — returns a generated password string.
  - `csv_library(pwd)` — appends `pwd` to `save.csv` in the current working directory.

## Usage (Windows)
1. Open a terminal and change to the project folder:
   cd c:\Users\LENOVO\Documents\Projects\password
2. Run the script:
   python app.py
3. Follow prompts:
   - Enter the desired password length (integer).
   - Answer y/n to include numbers.
   - Answer y/n to include special characters.
   - After the password is shown, choose to save it by selecting `1` (Yes) or `2` (No).

If you choose to save, the script appends the password to `save.csv` in the folder where you ran the script.

## Example session
- Enter length: `12`
- Numbers? `y`
- Special characters? `n`
- Generated password printed
- Save? `1` → password appended to `save.csv`

## Implementation notes
- `csv_library` uses `Path.cwd()` to determine the current working directory and opens `save.csv` with `newline=""` and `encoding="utf-8"` for proper CSV writing.
- `password_generator` builds a character pool from `string.ascii_letters` plus optional `string.digits` and `string.punctuation`. It ensures required types are present and returns a password string.

## Suggestions / Improvements
- Add argument parsing (argparse) for non-interactive use.
- Add input validation and clearer error messages.
- Add options to force at least one upper/lower/number/special character or to change allowed punctuation set.
- Consider encrypting saved passwords or storing them in a secure vault instead of plain CSV.

## License
Use as you wish.