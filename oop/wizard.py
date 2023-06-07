class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Name is required")
        self.name = name


class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def __str__(self):
        return f"{self.name} teaches {self.subject}"


if __name__ == "__main__":
    student = Student("Harry", "Gryffindor")
    professor = Professor("Goth", "Math")
    print(student)
    print(professor)
