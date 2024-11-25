import pandas as pd

FILENAME = "students.csv"

def read():
    return pd.read_csv(FILENAME, sep=":", names=["Имя", "Оценка"], header=None, encoding="utf-8")

def average(data):
    return data["Оценка"].mean()

def studentAverage(data):
    avg = average(data)
    belowAvg = data[data["Оценка"] < avg]
    print(f"Средняя оценка: {avg:.2f}")
    if belowAvg.empty:
        print("Нет студентов с оценками ниже среднего.")
    else:
        print("Студенты с оценками ниже среднего:")
        print(belowAvg)

def add(name, grade):
    new_data = pd.DataFrame({"Имя": [name], "Оценка": [grade]})
    new_data.to_csv(FILENAME, mode="a", index=False, header=False, sep=":", encoding="utf-8")
    print(f"Добавлен студент: {name} с оценкой {grade}")

def view():
    data = read()
    if data.empty:
        print("Нет данных для анализа.")
        return
    data["Оценка"] = pd.to_numeric(data["Оценка"], errors="coerce")
    studentAverage(data)

def main():
    while True:

        choice = input("Выберите действие: view, add, exit ")
        if choice == "view":
            view()
        elif choice == "add":
            name = input("Введите имя студента: ")
            grade = float(input("Введите оценку: "))
            add(name, grade)
        elif choice == "exit":

            break
        else:
            print("Попробуйте снова")

main()
