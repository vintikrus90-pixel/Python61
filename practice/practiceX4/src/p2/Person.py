class Person:
    def __init__(self, name: str, age: int, city: str):
        self.name = name
        self.age = age
        self.city = city
        self.role = Role.USER

    def set_role_admin(self):
        self.role = Role.ADMIN

    def get_role(self) -> Role:
        return self.role

    def get_personal_data(self) -> dict:
        return {"name": self.name, "age": self.age, "city": self.city}
