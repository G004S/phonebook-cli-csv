from datetime import datetime

phonebook = {}
def add_to_phonebook ():
    name = input("Insert person's name (format: Name Surname)\n: ")
    phone = input("Insert phone number\n: ")
    email = input("Insert person's email\n: ")
    now = datetime.now()
    date = now.strftime("%d.%m.%Y %H:%M")
    phonebook[name] = {'phone': phone, 'email': email, 'date': date}
    print(f"Added:\nName: {name} | Phone: {phone} | Email: {email} | Date: {date}")
    return
