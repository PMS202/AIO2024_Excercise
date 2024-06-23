from abc import ABC, abstractmethod


class ward():
    def __init__(self, name_ward: str):
        self.name_ward = name_ward
        self.person_list = []

    def add_person(self, info):
        self.person_list.append(info)

    def describe(self):
        print(f"Ward name: {self.name_ward}")
        for person in self.person_list:
            person.describe()

    def count_doctor(self):
        count = 0
        for person in self.person_list:
            if isinstance(person, doctor):
                count += 1
            else:
                continue
        return count

    def sort_age(self):
        # self.person_list.sort(key = lambda person : person.yob, reverse = True)

        for i in range(len(self.person_list)):
            for j in range(len(self.person_list) - i - 1):
                if self.person_list[j].yob < self.person_list[j+1].yob:
                    temp = self.person_list[j + 1].yob
                    self.person_list[j + 1].yob = self.person_list[j].yob
                    self.person_list[j].yob = temp
                else:
                    continue

    def compute_average(self):
        total = 0
        count = 0
        for person in self.person_list:
            if isinstance(person, teacher):
                total += person.yob
                count += 1
        return total/count


class person(ABC):
    def __init__(self, name: str, yob: int):
        self.name = name
        self.yob = yob

    @abstractmethod
    def describe(self):
        return f"Name: {self.name} - YoB: {self.yob}"


class student(person):
    def __init__(self, name: str, yob: int, grade: str):
        super().__init__(name, yob)
        self.grade = grade

    def describe(self):
        print(f"Student - {super().describe()} - Grade: {self.grade}")


class teacher(person):
    def __init__(self, name: str, yob: int, subject: str):
        super().__init__(name, yob)
        self.subject = subject

    def describe(self):
        print(f"Teacher - {super().describe()} - Subject: {self.subject}")


class doctor(person):
    def __init__(self, name: str, yob: int, specialist: str):
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self):
        print(f"Doctor - {super().describe()} - Specialist: {self.specialist}")


if __name__ == "__main__":

    student1 = student(name=" studentA ", yob=2010, grade="7")
    teacher1 = teacher(name=" teacherA ", yob=1969, subject=" Math ")
    doctor1 = doctor(name=" doctorA ", yob=1945,
                     specialist=" Endocrinologists ")
    teacher2 = teacher(name=" teacherB ", yob=1995, subject=" History ")
    doctor2 = doctor(name=" doctorB ", yob=1975, specialist=" Cardiologists ")
    ward1 = ward(name_ward=" Ward1 ")
    ward1 . add_person(student1)
    ward1 . add_person(teacher1)
    ward1 . add_person(teacher2)
    ward1 . add_person(doctor1)
    ward1 . add_person(doctor2)

    # 2 (b)
    ward1 . describe()
    # 2(c)
    print(f"\nNumber of doctors : { ward1 . count_doctor ()}")
    # 2(d)
    print("\nAfter sorting Age of Ward1 people ")
    ward1 . sort_age()
    ward1 . describe()
    # 2 (e)
    print(
        f"\nAverage year of birth ( teachers ): { ward1 . compute_average ()}")
