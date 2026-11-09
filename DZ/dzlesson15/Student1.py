# Домашнее задание 15
# Класс и логика работы с оценками

class Student:
    students = []

    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grades(self, grades):
        for grade in grades:
            if Student.is_valid_grade(grade):
                self.grades.append(grade)

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    @classmethod
    def average_all(cls):
        all_grades = []
        for student in cls.students:
            all_grades.extend(student.grades)
        if not all_grades:
            return 0
        return sum(all_grades) / len(all_grades)

    @staticmethod
    def is_valid_grade(grade):
        return isinstance(grade, int) and 1 <= grade <= 5
