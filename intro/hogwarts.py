#!/usr/bin/env python

def main():
    students = ["Hermione", "Harry", "Ron"]
    house = {
        "Hermione": "Griffindor",
        "Harry": "Griffindor",
        "Ron": "Griffindor",
        "Draco": "Slytherin",
    }

    records = [
        {"name": "Hermione", "house": "Griffindor", "patronus": "Otter"},
        {"name": "Harry", "house": "Griffindor", "patronus": "Stag"},
        {"name": "Ron", "house": "Griffindor", "patronus": "Jack Russell terrier"},
        {"name": "Draco", "house": "Slytherin", "patronus": None},
    ]

    for record in records:
        print(record)

    for k in house:
        print(k, house[k])

    for student in students:
        print(student)

    for i in range(len(students)):
        print(i + 1, students[i])

    for i, student in enumerate(students):
        print(i + 1, student)


if __name__ == "__main__":
    main()



