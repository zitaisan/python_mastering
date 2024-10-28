passw = input("Введите пароль: ")
ln = False
dig = False
upp = False
symb = False
if len(passw) >= 8:
    ln = True
for char in passw:
    if char.isdigit():
        dig = True
    if char.isupper():
        upp = True
    if char in ("!@#.,"):
        symb = True
if not ln or not dig or not upp or not symb:
    print("Пароль не прошел проверку:")
    print(ln,dig,upp,symb)
    if not(ln):
        print("Длина пароля должна быть не менее 8 символов.")
    if not(dig):
        print("Пароль должен содержать хотя бы одну цифру.")
    if not(upp):
        print("Пароль должен содержать хотя бы одну заглавную букву.")
    if not(symb):
        print("Пароль должен содержать хотя бы один специальный символ.")
else:
    print("Пароль прошел проверку!")




