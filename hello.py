from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self._name = name
        self.__age = age

    @abstractmethod
    def get_role(self):
        pass

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @age.deleter
    def age(self):
        del self.__age


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.__grade = grade

    def get_role(self):
        return "Student"

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, value):
        self.__grade = value

    @grade.deleter
    def grade(self):
        del self.__grade


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.__subject = subject

    def get_role(self):
        return "Teacher"

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, value):
        self.__subject = value

    @subject.deleter
    def subject(self):
        del self.__subject


class Room:
    def __init__(self):
        self.__people = []

    def add_person(self, person):
        self.__people.append(person)

    def get_students(self):
        return [p for p in self.__people if isinstance(p, Student)]

    def get_teachers(self):
        return [p for p in self.__people if isinstance(p, Teacher)]

    def delete_student(self, name):
        self.__people = [p for p in self.__people if not (isinstance(p, Student) and p.name == name)]

    def count_students(self):
        return len(self.get_students())

    def count_successful_students(self):
        return len([s for s in self.get_students() if s.grade >= 50])

    @property
    def people(self):
        return self.__people

    @people.setter
    def people(self, value):
        self.__people = value

    @people.deleter
    def people(self):
        del self.__people
