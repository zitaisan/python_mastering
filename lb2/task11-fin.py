import random

month = float(input("Введите ваш ежемесячный доход: "))
num = int(input("Введите количество категорий расходов: "))
expenses = []
for _ in range(num):
    expense = float(input("Введите расходы на категорию: "))
    expenses.append(expense)
total = month
minus = sum(expenses)
balance = total - minus
print(f"Общий доход: {total} руб.")
print(f"Общие расходы: {minus} руб.")
print(f"Остаток: {balance} руб.")
suggestions = [
        "уменьшить траты на развлечения",
        "сократить расходы на транспорт",
        "проверить расходы на продукты",
        "сократить расходы на одежду"
    ]

if balance < 0:
    print("Ваш остаток отрицательный. Рекомендуем:")
    print(random.choice(suggestions))

# Расчет возможных накоплений за год
res = balance * 12
if balance >= 0:
    print(f"Вы сможете накопить {res} руб. за год.")
