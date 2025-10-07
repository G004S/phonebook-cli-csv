from datetime import datetime
from .validators import normalize_phone, validate_email

phonebook = {}

def add_to_phonebook():
    name = input("Insert person's name (format: Name Surname)\n: ").strip()
    if not name:
        print("Name cannot be empty")
        return

    while True:
        phone_raw = input("Insert phone number\n: ").strip()
        try:
            phone = normalize_phone(phone_raw)
            break
        except ValueError as e:
            print(f"{e}. Try again.")


    while True:
        email_raw = input("Insert person's email (press Enter to skip)\n: ").strip()
        try:
            email = validate_email(email_raw)
            break
        except ValueError as e:
            print(f"{e}. Try again.")


    now = datetime.now()
    date = now.strftime("%d.%m.%Y %H:%M")

    phonebook[name] = {'phone': phone, 'email': email, 'date': date}
    print(f"Added:\nName: {name} | Phone: {phone} | Email: {email or '—'} | Date: {date}")
    return
