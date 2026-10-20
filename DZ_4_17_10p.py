# Домашнее задание 4
name = input("Введите имя : ").capitalize()
surname = input("Введите фамилию : ").capitalize()
message = input("Введите текст сообщение : ")

if not name or not surname or not message:
    print("система не принимает пустые значения")
else:
    letter = (
        f"Уважаемый {name} {surname},\n"
        f"{message}\n"
        f"С уважением, {name} {surname}"
    )
    print("\n" + letter)