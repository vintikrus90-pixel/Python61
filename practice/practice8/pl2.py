class DBConnection:
    def __enter__(self):
        print("открываем соединение с базой данных")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("закрываем соединение с базой данных")

        if exc_type:
            print(f"ошибка такая то: {exc_val}")
        return True


with DBConnection() as db:
    print("работа с базой данных")
    raise Exception("что то пошло не так")
