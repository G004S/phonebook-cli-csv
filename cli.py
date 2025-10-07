from src.phonebook.app import phonebook, add_to_phonebook
from datetime import datetime
from src.phonebook.database import save_to_csv, load_from_csv, ensure_csv_initialized, delete_from_phonebook
ensure_csv_initialized()
print(load_from_csv())
phonebook.update(load_from_csv())
while True:
    menu = input("Main menu:\n[1] --> Add person to phonebook\n[2] --> Delete from phonebook\n[0] --> Exit\n")
    if menu == "1":
        add_to_phonebook()
        save_to_csv(phonebook)
    elif menu == "2":
        delete_from_phonebook()
    elif menu == "0":
        break
