# Задача: реализовать менеджер контекста для работы с кэшом.
# Менеджер должен хранить кэш в словаре и автоматически очищать
# его при выходе из блока with.

class CacheManager:
    def __enter__(self):
        print("открываем кэш")
        self.cache = {}
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("очищаем кэш")

        if exc_type:
            print(f"ошибка такая то: {exc_val}")

        self.cache.clear()
        return True


with CacheManager() as cache:
    cache.cache["ключ1"] = "значение1"
    cache.cache["ключ2"] = "значение2"
    print("работа с кэшем:", cache.cache)
