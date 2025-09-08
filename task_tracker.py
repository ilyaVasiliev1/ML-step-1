class Task:
    def __init__(self, name, desc, deadline):
        self.name = name
        self.desc = desc
        self.deadline = deadline

task_array = []

while True:
    user_text = input("Введите команду: ")
    if user_text == "add_task":
        task_name = input("Введите название задачи: ")
        task_desc = input("Введите описание задачи: ")
        task_deadline = input("Введите дату окончания: ")
        task_array.append(Task(name=task_name, desc=task_desc, deadline=task_deadline))

    elif user_text == "remove_task":
        for idx, task in enumerate(task_array):
            print(idx, task.name)
        task_index = int(input("Введите индекс задачи, которую нужно удалить: "))
        if 0 <= task_index < len(task_array):
            task_array.pop(task_index)
        else:
            print("Неверный индекс!")

    elif user_text == "info_task":
        for idx, task in enumerate(task_array):
            print(idx, task.name, "-", task.desc, "-", task.deadline)
