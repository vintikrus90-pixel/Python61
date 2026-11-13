from functools import wraps

def authorize_user(func):  # 1 usage
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if user.get("role") == "admin":
            return func(user, *args, **kwargs)
        else:
            print(f"Доступ запрещён для {user.get('name')}")
            return None
    return wrapper

@authorize_user  # 2 usages
def update_profile(user, profile_data):
    """ test """
    print(f"{user.get('name')} обновил профиль с данными: {profile_data}")

update_profile({"name": "Alice", "role": "admin"}, {"age": 25, "city": "Москва"})
update_profile({"name": "Bob", "role": "user"}, {"age": 25, "city": "Москва"})
