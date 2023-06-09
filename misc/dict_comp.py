students = ["Hermione", "Harry", "Ron"]

gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]
print(gryffindors)

gryffindors = {student: "Gryffindor" for student in students}
print(gryffindors)

for i, s in enumerate(students, start=10):
    print("%02d\t%s" % (i, s))

