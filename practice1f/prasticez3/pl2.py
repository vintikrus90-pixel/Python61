task_tree = {
    "name": "Main Task",
    "subtasks": [
        {"name": "Subtask 1", "subtasks": []},
        {"name": "Subtask 2", "subtasks": [
            {"name": "Sub-subtask 1", "subtasks": []},
            {"name": "Sub-subtask 2", "subtasks": []},
        ]},
    ],
}

def count_tasks(task_tree):
    # Базовый случай: если подзадач нет, возвращаем 1 (только сама задача).
    if not task_tree.get("subtasks"):
        return 1
    # Рекурсивный случай: 1 за текущую задачу + сумма по всем подзадачам.
    return 1 + sum(count_tasks(subtask) for subtask in task_tree["subtasks"])

print(count_tasks(task_tree))
