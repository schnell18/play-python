def is_grayffindor(s):
    return s["house"] == "Gryffindor"


if __name__ == "__main__":
    students = [
        {"name": "Hermione", "house": "Gryffindor"},
        {"name": "Harry", "house": "Gryffindor"},
        {"name": "Ron", "house": "Gryffindor"},
        {"name": "Draco", "house": "Slytherin"},
        {"name": "Padma", "house": "Ravenclaw"},
    ]

    houses = set()
    for student in students:
        houses.add(student["house"])

    for house in sorted(houses):
        print(house)

    gryffindors = map(lambda s: s["name"], filter(is_grayffindor, students))
    for s in gryffindors:
        print(s)

    gryffindors = [s for s in students if is_grayffindor(s)]
    print(gryffindors)
