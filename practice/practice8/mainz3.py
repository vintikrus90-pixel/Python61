class MyContextManager:
    def __enter__(self):
        print("Входим в контекст")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Выходим из контекста")
        if exc_type:
            # Логируем ошибку
            print(f"Произошло исключение: {exc_value}")
            # Не возвращаем True, чтобы исключение всплыло дальше
        return True

with MyContextManager():
    print("Внутри контекстного менеджера")
    raise ValueError("Это ошибка!")