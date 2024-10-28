import random as r
dig = list(map(int, input("Введите числа: ").split()))
print(dig)
r.shuffle(dig)
print(dig, "min", min(dig), "max", max(dig))