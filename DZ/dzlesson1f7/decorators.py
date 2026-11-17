# Домашнее задание 17
# Действий пользователя

import datetime
from functools import wraps

def log_action(action_name):
    def decorator(func):
        @wraps(func)
        def wrapper(self,*args, **kwargs):
            time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"[{time_now}] Выполняется :  {action_name}")
            return func(self,*args, **kwargs)
        return wrapper
    return decorator