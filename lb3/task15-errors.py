import datetime
FILENAME = "errors.log"
def add(message):
    with open(FILENAME, "a", encoding="utf-8") as log_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{timestamp}] {message}\n")
    print(f"Ошибка записана: {message}")


def view(count=5):
    with open(FILENAME, "r", encoding="utf-8") as log_file:
        lines = log_file.readlines()
        if not lines:
            print("Файл с логами пуст.")
            return
        print(f"Последние {min(count, len(lines))} ошибок:")
        for line in lines[-count:]:
            print(line.strip())
def clear():
    open(FILENAME, "w", encoding="utf-8").close()


def main():
    while True:
        choice = input("Выберите действие: add, view, clear, exit ")

        if choice == "add":
            try:
                number = int(input("Введите целое число: "))
                print(f"Вы ввели число: {number}")
            except ValueError as e:
                add(e)
        elif choice == "view":
            view()
        elif choice == "clear":
            clear()
        elif choice == "exit":
            exit()
        else:
            print("Попробуйте снова")
main()
