currencies = {
    "USD": 75,
    "EUR": 90}

def convertCurrency(rub, currency):
    """Конвертирует сумму в рублях в выбранную валюту."""
    if currency in currencies:
        amount = rub / currencies[currency]
        print(f"{rub} RUB = {amount} {currency}")
    else:
        print("Ошибка")

def addCurrency():
    currency = input("Введите название валюты: ").upper()
    if currency in currencies:
        print("Валюта уже существует")
    else:
        try:
            currencies[currency] = float(input(f"Введите курс для {currency}: "))
            print(f"Добавлена валюта {currency}")
        except Exception as e:
            print(f"Ошибка: {e}")


def updateCurrency():
    currency = input("Введите название валюты: ").upper()
    try:
        new_rate = float(input(f"Введите курс для {currency}: "))
        currencies[currency] = new_rate
        print("Успешно")
    except Exception as e:
        print(f"Ошибка: {e}")



def removeCurrency():
    global currencies
    currency = input("Введите валюту для удаления: ").upper()
    if currency in currencies:
        del currencies[currency]
        print(f"Валюта {currency} удалена")
    else:
        print("Валюта не найдена")


def showCurrency():
    print("Текущие курсы валют:")
    for currency, rate in currencies.items():
        print(f"{currency}: {rate}")


def main():
    while True:
        choice = input("Выберите действие convert, show, add, update, exit, remove: ")
        if choice == "convert":
            try:
                rub = float(input("Введите сумму в рублях: "))
                currency = input("Введите валюту: ")
                convertCurrency(rub, currency)
            except Exception as e:
                print(f"Ошибка: {e}")
        elif choice == "update":
            updateCurrency()
        elif choice == "add":
            addCurrency()
        elif choice == "remove":
            removeCurrency()
        elif choice == "show":
            showCurrency()
        elif choice == "exit":
            exit()
        else:
            print("Попробуйте еще раз")

main()
