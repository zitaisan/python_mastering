menu = (
)
def checkDishes(budget):

    checked = list(filter(lambda dish: dish[1] <= budget, menu))
    if checked:
        print("Блюда:")
        for dish in checked:
            print(f"{dish[0]} - {dish[1]} руб.")
    else:
        print("Нет такого блюда")

def addDish(name, price):
    global menu
    menu += ((name, price),)
    print(f"Блюдо '{name}' добавлено")


def updateDish(name, new_price):
    global menu
    update = []
    found = False

    for dish in menu:
        if dish[0] == name:
            update.append((name, new_price))
            found = True
            print(f"Цена блюда '{name}' обновлена")
        else:
            update.append(dish)

    if not found:
        print("Блюдо не найдено в меню")

    menu = tuple(update)

def showDishes():
    for dish in menu:
        print(f"{dish[0]} - {dish[1]} руб.")
def main():
    while True:
        comm = input("\nВведите команду (show, check, add, update, exit): ").lower()

        if comm == "show":
            print("Текущее меню:")
            showDishes()
        elif comm == "check":
            try:
                checkDishes(int(input("Введите ваш бюджет: ")))
            except Exception as e:
                print(f"Ошибка: {e}")

        elif comm == "add":
            name = input("Введите название нового блюда: ")
            try:
                price = int(input("Введите цену нового блюда: "))
                addDish(name, price)
            except Exception as e:
                print(f"Ошибка: {e}")

        elif comm == "update":
            name = input("Введите название блюда для обновления: ")
            try:
                new_price = int(input("Введите новую цену: "))
                updateDish(name, new_price)
            except Exception as e:
                print(f"Ошибка: {e}")

        elif comm == "exit":
            exit()

        else:
            print("Попробуйте снова")

main()
