class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Name is required!")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get_student_as_object(cls):
        name = input("Name: ")
        house = input("House: ")
        patronus = input("Patronus: ")
        return Student(name, house, patronus)

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house!")
        self._house = house

    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐴"
            case "Otter":
                return "🐌"
            case "Jack Russell terrier":
                return "🐶"
            case _:
                return "🖊"


def main():
    # name, house = get_student()
    # print(f"{name} from {house}")
    # student = get_student_as_tuple()
    # print(f"{student[0]} from {student[1]}")
    # student = get_student_as_list()
    # print(f"{student[0]} from {student[1]}")
    # student = get_student_as_dict()
    # print(f"{student['name']} from {student['house']}")
    student = Student.get_student_as_object()
    # student.house = "People's square 200"
    student._house = "People's square 200"
    print("Expecto Patronum")
    print(student.charm())
    print(student)


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
    patronus = input("Patronus: ")
    student = Student(name, house, patronus)
    return student


if __name__ == "__main__":
    main()
