# 📞 Phonebook CLI

A simple command-line phonebook application written in **Python**.  
Contacts are stored in a **CSV file** and loaded automatically on startup.  
Project created as part of my Python learning journey.

---

## 🚀 Features

- Add new contacts with name, phone, email, and creation date with email and phone number validation through regex
- View all contacts  
- Remove existing contacts  
- Persistent CSV storage  
- Automatically creates the CSV file if it doesn't exist  
- Simple and beginner-friendly codebase

---

## 🧩 Project Structure

phonebook-cli-csv/
├── src/
│ └── phonebook/
│ ├── app.py
│ ├── database.py 
│ ├── validators.py
│ └── init.py
├── data/
│ └── .gitkeep
├── .gitignore
├── cli.py
└── README.md

---

## ⚙️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/G004S/phonebook-cli-csv.git
   cd phonebook-cli-csv

2. Run the CLI app:
    py -3 -m src.phonebook.main

3. Follow on-screen menu:
    [1] Add new contact
    [2] Show all contacts
    [3] Remove contact
    [0] Exit

--- 

## 🛠 Requirements
    Python 3.10+
    No external libraries required (uses built-in csv and datetime)

---

## 🧠 Learning Goals
This project was created to practice:
    Working with CSV files
    Using dictionaries for data storage
    Handling exceptions
    Using regex
    Structuring a Python project
    Implementing simple CRUD logic (Create, Read, Update, Delete)

---

## 📅 Future Improvements
    Add search by name
    Export contacts to JSON
    Add unit tests

---

## ✍️ Author
    Georgii Senotrusov
    📍 Finland
    https://github.com/G004S
