class CacheManager:
    def __init__(self):
        self.cache = {}

    def __enter__(self):
        print("Открываем кэш")
        return self.cache  # Возвращаем словарь, чтобы работать с ним через as

    def __exit__(self, exc_type, exc_value, traceback):
        print("Очищаем кэш")
        self.cache.clear()

        if exc_type:
            print(f"Произошла ошибка: {exc_value}")
        return True  # Если возвращаем True, исключение не будет поднято


# Использование
with CacheManager() as cache:
    cache["user:1"] = "Анна"
    cache["user:2"] = "Иван"
    print("Работаем с кэшем:", cache)
