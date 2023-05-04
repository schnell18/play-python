import csv

name = input("What's your name? ")
home = input("Where's the home? ")
with open("students-entry.csv", "a") as file:
    writer = csv.writer(file);
    writer.writerow([name, home])

with open("students-entry-dict.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"]);
    writer.writerow({"name": name, "home": home})
