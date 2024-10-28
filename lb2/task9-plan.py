tasks = []
for i in range(5):
    task = input(f"Введите задачу {i + 1}: ")
    tasks.append(task)
numb = int(input("Введите номер выполненной задачи: "))
tasks.remove(tasks[numb - 1])
print(tasks)
