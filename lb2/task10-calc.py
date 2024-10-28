km = float(input("km: "))
lt = float(input("litres: "))
ct = input("car type: ")
avlt = (lt/km)*100
print("Средний расход топлива:", avlt)
# Проверка нормы расхода по типу автомобиля
if ct == "малолитражка":
    olt = 5
elif ct == "средний":
    olt = 7
elif ct == "внедорожник":
    olt = 12
else:
    print("Неизвестно")
    optimal_consumption = None
if olt:
    print("Оптимальный расход:", olt)
    if avlt>olt:
        print("Сократите расход!")
elif avlt>10:
    print("Сократите расход!")
