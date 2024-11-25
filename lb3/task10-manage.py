import os
FILENAME = "tasks.txt"
def load():
    tasks = []
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            for line in file:
                title, category = line.strip().split(" | ")
                tasks.append({"title": title, "category": category})
    return tasks
def save(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(f"{task['title']} | {task['category']}\n")
def add(tasks):
    title = input("Введите название задачи: ")
    category = input("Введите категорию задачи (например, 'важные', 'личные'): ")
    tasks.append({"title": title, "category": category})
    save(tasks)
    print("Задача добавлена.")
def edit(tasks):
    view(tasks)
    index = int(input("Введите номер задачи для редактирования: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index]["title"] = input("Введите новое название задачи: ")
        tasks[index]["category"] = input("Введите новую категорию задачи: ")
        save(tasks)
        print("Задача отредактирована.")
    else:
        print("Неверный номер задачи.")

def delete_task(tasks):
    view(tasks)
    index = int(input("Введите номер задачи для удаления: ")) - 1
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save(tasks)
        print("Задача удалена")
    else:
        print("Неверный номер задачи")

def view(tasks):
    if tasks:
        print("\nСписок всех задач:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['title']} [{task['category']}]")
    else:
        print("Список задач пуст")

def viewByCategory(tasks):
    category = input("Введите категорию для фильтрации задач: ")
    filtered_tasks = [task for task in tasks if task["category"].lower() == category.lower()]
    if filtered_tasks:
        print(f"\nЗадачи в категории '{category}':")
        for i, task in enumerate(filtered_tasks, 1):
            print(f"{i}. {task['title']}")
    else:
        print(f"Нет задач в категории '{category}'.")

def main():
    tasks = load()
    while True:
        choice = input("Выберите действие add, edit, delete, viewtask, viewbycateg, exit: ")
        if choice == "add":
            add(tasks)
        elif choice == "edit":
            edit(tasks)
        elif choice == "delete":
            delete_task(tasks)
        elif choice == "viewtask":
            view(tasks)
        elif choice == "viewbycateg":
            viewByCategory(tasks)
        elif choice == "exit":
            print("Выход из программы.")
            break
        else:
            print("Попробуйте снова")

main()
