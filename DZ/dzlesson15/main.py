# Домашнее задание 15
# Консольный интерфейс и обработка команд

from dzlesson15.Student1 import Student

while True:
    cmd = input("Команды <add>(Добавить студента)/"
                "<grades>(Добавить оценки)/"
                "<show>(Средняя оценка студента)/"
                "<all>(Средняя всех)/"
                "<check>(Проверить оценк)/"
                "<exit>/ : ")

    if cmd == "add":
        name = input("<Имя : ")
        student = Student(name)
        Student.students.append(student)
        print(f'Студент "{name}" добавлен')

    elif cmd == "grades":
        name = input("<Имя : ")
        if not any(s.name == name for s in Student.students):
            print(f'Студент "{name}" нет')
            continue
        student = next(s for s in Student.students if s.name == name)
        raw = input("Оценка через пробел (от 1 до 5) : ")
        grades = [int(g) for g in raw.split()]
        student.add_grades(grades)
        print(f"Оценка : {student.grades}")

    elif cmd == "show":
        name = input("<Имя : ")
        if not any(s.name == name for s in Student.students):
            print(f'Студент "{name}" нет')
            continue
        student = next(s for s in Student.students if s.name == name)
        print(f'Средняя оценка "{name}" : {student.average_grade():.2f}')

    elif cmd == "all":
        print(f"Средняя оценка всех студентов : {Student.average_all():.2f}")

    elif cmd == "check":
        grade = int(input("Оценка : "))
        if Student.is_valid_grade(grade):
            print("Допустима")

    elif cmd == "exit":
        break
