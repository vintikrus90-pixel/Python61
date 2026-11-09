# Домашнее задание 16
# Должность и отображение информации

from dzlesson16.Person import Person

class Employee(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position

    def get_position(self):
        return self.position

    def get_info(self):
        return f"{self.get_name()} {self.get_age()} лет, должность :  {self.position}"