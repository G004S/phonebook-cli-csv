import csv
import os

PATH = r"C:/Users/uespu/Desktop/Phone_Book/data/phonebook.csv"
FIELDNAMES = ["name", "phone", "email", "date"]

def ensure_csv_initialized():
    if not os.path.exists(PATH):
        with open(PATH, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES, delimiter=",")
            writer.writeheader()
        return

    with open(PATH, "r", encoding="utf-8") as f:
        first_line = f.readline()

    if not first_line:
        with open(PATH, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES, delimiter=",")
            writer.writeheader()
        return

    header = [h.strip() for h in first_line.strip().split(",")]
    if header != FIELDNAMES:
        rows = []
        with open(PATH, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                rows.append(line.split(","))

        with open(PATH, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES, delimiter=",")
            writer.writeheader()
            for row in rows:
                if len(row) == 4 and row != FIELDNAMES:
                    writer.writerow(dict(zip(FIELDNAMES, row)))

def load_from_csv():
    ensure_csv_initialized()
    loaded = {}
    with open(PATH, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f, fieldnames=FIELDNAMES, delimiter=",")
        next(reader, None)
        for row in reader:
            name = row["name"]
            if not name:
                continue
            loaded[name] = {
                "phone": row["phone"],
                "email": row["email"],
                "date": row["date"],
            }
    return loaded

def save_to_csv(phonebook):
    ensure_csv_initialized()
    with open(PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES, delimiter=",")
        writer.writeheader()
        for name, info in phonebook.items():
            writer.writerow({
                "name": name,
                "phone": info.get("phone", ""),
                "email": info.get("email", ""),
                "date": info.get("date", ""),
            })

def delete_from_phonebook():
    ensure_csv_initialized()
    dlt = input("Insert a person's name. The person will be deleted from the phonebook\n: ")
    with open (PATH, "r", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        rows = []
        for row in reader:
            if row["name"] != dlt:
                rows.append(row)
        
    fieldnames = ["name","phone","email","date"]
    with open(PATH, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Deleted: {dlt} if existed")