import csv

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append({
            'name': name,
            'house': house,
        })

def byName(a):
    return a['name']

for student in sorted(students, key=byName, reverse=False):
    print(f"{student['name']} => {student['house']}")

for student in sorted(students, key=lambda a: a['name'], reverse=False):
    print(f"{student['name']} => {student['house']}")


students = []
with open("students2.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append({
            'name': row[0],
            'home': row[1],
        })

for student in sorted(students, key=lambda a: a['name'], reverse=False):
    print(f"{student['name']} => {student['home']}")


