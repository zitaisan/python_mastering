products = {}
def addProduct():
    name = input("Введите название продукта: ")
    price = float(input(f"Введите цену продукта {name}: "))
    products[name] = price
    print(f"Продукт '{name}' добавлен")
def searchProduct():
    name = input("Введите название продукта для поиска: ")
    if name in products:
        print(f"Цена продукта '{name}': {products[name]} руб.")
    else:
        print(f"Продукт '{name}' не найден")
def editPrice():
    name = input("Введите название продукта: ")
    if name in products:
        new_price = float(input(f"Введите новую цену для '{name}': "))
        products[name] = new_price
        print(f"Цена продукта '{name}' обновлена.")
    else:
        print(f"Продукт '{name}' не найден.")


def deleteProduct():
    name = input("Введите название продукта для удаления: ")
    if name in products:
        del products[name]
        print(f"Продукт '{name}' удален.")
    else:
        print(f"Продукт '{name}' не найден.")


def showProducts():
    if products:
        print("Список продуктов:")
        for name, price in products.items():
            print(f"{name}: {price} руб.")
    else:
        print("Пусто")


def main():
    while True:
        choice = input("Выберите действие: add, search, edit, delete, show, exit: ")

        if choice == 'add':
            addProduct()
        elif choice == 'search':
            searchProduct()
        elif choice == 'edit':
            editPrice()
        elif choice == 'delete':
            deleteProduct()
        elif choice == 'show':
            showProducts()
        elif choice == 'exit':
            exit()
        else:
            print("Попробуйте снова.")

main()
