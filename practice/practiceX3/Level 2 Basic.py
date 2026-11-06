# Уровень 2: Средний
# Задача: напишите программу,
# которая позволяет пользователю добавлять и удалять фильмы из списка любимых фильмов.
# Пользователь должен ввести команду ‘add’ для добавления фильма или ‘remove’ для его удаления.
# После каждого действия программа должна выводить обновленный список.

favorite_movies = []

print("Менеджер фильмов")
print("команды add - добавить фильм remove - удалить фильм exit - выйти \n")

while True:
    command = input("Введите команду : ").strip().lower()

    if command == "add":
        movie = input("Название фильма : ").strip()
        favorite_movies.append(movie)
        print("Фильм добавлен\n")


    elif command == "remove":
        movie = input("Название фильма для удаления : ").strip()
        if movie in favorite_movies:
            favorite_movies.remove(movie)
            print("Фильм удален\n")

    elif command == "exit":
        break

    if command in ("add", "remove"):
        if favorite_movies:
            print("Список : ")
            for movie in favorite_movies:
                print(movie)