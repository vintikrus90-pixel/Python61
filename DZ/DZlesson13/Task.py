# Домашнее задание 13
# Модель одной задачи

class Task:
    def __init__(self, title):
        self.title = title
        self.is_done = False

    def mark_done(self):
        self.is_done = True

    def to_dict(self):
        return {'title': self.title, 'is_done': self.is_done}

    @classmethod
    def from_dict(cls, data):
        return cls(data['title'])