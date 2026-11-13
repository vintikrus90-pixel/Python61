def log_transactions(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Лог : {func.__name__}({args[1:]})  {result}")
        return result
    return wrapper
