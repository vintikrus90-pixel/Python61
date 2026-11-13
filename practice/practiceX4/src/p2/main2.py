from functools import wraps
from Role import Role
from practiceX4.src.p2.Person import Person


def authorize_user(func):
    @wraps(func)
    def wrapper(user: Person, *args, **kwargs):
        if user.get_role() in (Role.ADMIN, Role.MANAGER):
            return func(user, *args, **kwargs)
        else:
            print(f"Доступ запрещён для {user.name}")
            return None
    return wrapper


@authorize_user
def update_profile(user: Person):
    """test"""
    print(f"{user.name} обновил профиль с данными: {user.get_personal_data()}")


user1 = Person(name="Alice", age=25, city="Москва")
user2 = Person(name="Bob", age=25, city="Москва")

user1.set_role_admin()

update_profile(user1)
update_profile(user2)
