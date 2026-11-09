# Домашнее задание 16
# Команда сотрудников

from dzlesson16.Employee import Employee

class Manager(Employee):
    def __init__(self, name, age, position):
        super().__init__(name, age, position)
        self.team = []

    def add_to_team(self, employee):
        self.team.append(employee)

    def show_team(self):
        print(f"Команда менеджера {self.get_name()} : ")
        for member in self.team:
            print(f"{member.get_info()}")
