class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house


def main():
    # name, house = get_student()
    # print(f"{name} from {house}")
    # student = get_student_as_tuple()
    # print(f"{student[0]} from {student[1]}")
    # student = get_student_as_list()
    # print(f"{student[0]} from {student[1]}")
    # student = get_student_as_dict()
    # print(f"{student['name']} from {student['house']}")
    student = get_student_as_object()
    print(f"{student.name} from {student.house}")


def get_name():
    return input("Name: ")


def get_house():
    return input("House: ")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house


def get_student_as_tuple():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)


def get_student_as_list():
    name = input("Name: ")
    house = input("House: ")
    return [name, house]


def get_student_as_dict():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student


def get_student_as_object():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student


if __name__ == "__main__":
    main()
