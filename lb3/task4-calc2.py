discounts = {
        '10%': lambda price: price * 0.9,
        '20%': lambda price: price * 0.8,
        '50 на покупку свыше 1000': lambda price: price * 0.5 if price > 300 else price,
    }
prices=[]
def calcDiscount(prices, discount):
    return [discount(price) for price in prices]
def addPrices():
    global prices
    print("Введите цены: ")
    comm = ''
    try:
        prices = list(map(float, input().split(' ')))
    except Exception as e:
        print(f'Ошибка: {e}')
def showDiscount():
    for discount in discounts:
        print(discount)

def main():

    addPrices()

    print('Введите выбранный тип скидки:')
    showDiscount()
    choice = input()
    if choice in discounts:
        discount = discounts[choice]
        print("Цены после применения скидки:", calcDiscount(prices, discount))
    else:
        print("Попробуйте еще раз.")
main()
