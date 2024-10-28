x = input("Введите строку: ")
print("Количество символов с пробелами:", len(x))
vow = "аеёиоуыэюяАЕЁИОУЫЭЮЯaeiouAEIOU"
c_vow = 0
for char in x:
    if char in vow:
        c_vow+=1
print("Количество гласных букв:", c_vow)
s_x = x.split()
print("Слова:")
for word in s_x:
    print(word)
u_x=set(s_x)
print("Уникальные:")
for word in u_x:
    print(word)