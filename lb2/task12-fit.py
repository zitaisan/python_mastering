stepsAll = []
for day in range(7):
    steps = int(input(f"Введите количество шагов, пройденных в день {day + 1}: "))
    stepsAll.append(steps)

total = sum(stepsAll)
av = total / len(stepsAll)
print("Общее количество шагов за неделю:", total)
print("Среднее количество шагов в день:", av)

for day, steps in enumerate(stepsAll, start=1):
    if steps > 10000:
        print(f"В день {day} вы прошли более 10,000 шагов!")

calories = total * 0.05
print(f"Общее количество сожженных калорий: {calories:.2f} калорий")
