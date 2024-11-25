import os
FILENAME = "tasks.txt"
def read():
    data = {}
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            for line in file:
                if line.strip():
                    product, quantity, price = line.strip().split('\t')
                    quantity = int(quantity)
                    price = float(price)
                    total = quantity * price

                    if product in data:
                        data[product] += total
                    else:
                        data[product] = total

    return data
def add(product,quantity,price):
    with open(FILENAME, 'a') as file:
        file.write(f"{product}\t{quantity}\t{price}\n")
def find(data):
    if not data:
        return None, None
    max_p = max(data, key=data.get)
    min_p = min(data, key=data.get)
    return max_p, min_p



def summ(sales_data):
    max_product, min_product = find(sales_data)

    if max_product and min_product:
        print(f"Продукт с наибольшей суммой продаж: {max_product} - {sales_data[max_product]:.2f} руб.")
        print(f"Продукт с наименьшей суммой продаж: {min_product} - {sales_data[min_product]:.2f} руб.")
    else:
        print("Нет данных")



def main():
    while True:
        data = read()
        summ(data)
        addD= input("\nЕсли хотите добавить данные, введите да (для выхода нажмите exit): ").strip().lower()

        if addD == 'да':
            product = input("Введите название продукта: ").strip()
            quantity = int(input("Введите количество: "))
            price = float(input("Введите цену: "))

            add(product, quantity, price)
            data = read()

            print("\nОбновленная информация о продажах:")
            summ(data)
        elif addD=='exit':
            exit()


main()
