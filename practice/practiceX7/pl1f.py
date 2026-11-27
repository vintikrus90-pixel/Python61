from collections import deque

class TaskQueue:
    def __init__(self, max_len):
        self.queue = deque(maxlen=max_len)
    def add_task(self, task):
        self.queue.append(task)
    def get_tasks(self):
        return list(self.queue)


tq = TaskQueue(10)
tq.add_task(1)
tq.add_task("помыть пол")
tq.add_task(3)
tq.add_task(1)
tq.add_task(3)
tq.add_task(3)
tq.add_task(3)
tq.add_task(3)
tq.add_task(3)
tq.add_task(3)
tq.add_task(3)
tq.add_task(5)
print(tq.get_tasks())
