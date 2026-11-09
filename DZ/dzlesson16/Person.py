# Домашнее задание 16
# Имя и возраст

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_info(self):
        return f"{self.name} {self.age} лет"