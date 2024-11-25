calc = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y if y != 0 else 'Ошибка: деление на ноль'
}

res = 0.0
def useOperation(dig1, dig2, name):
    if name in calc:
        res = calc[name](dig1, dig2)
        return f'Ваш реузльтат: {res}'
    else:
        return 'Нет такой операции'
def addOperation(name):
    if name in calc:
        return 'Операция существует в словаре'
    else:
        operationAdd = input(
            f"Введите лямбда-выражение для операции '{name}':\nнапример, для '^' введите 'lambda x, y: x ** y'\n> ")
        try:
            calc[name] = eval(operationAdd)
            return f'Операция {name} теперь в словаре'
        except Exception as e:
            print("Ошибка:", e)
            return
def showOperation():
    print('Операции в словаре:')
    for x in calc:
        print(x)
def main():
    comm=''
    while comm != 'exit':
        dig1, dig2 = 0, 0
        name = ''
        comm = input('Введите название команды: use, add, show, exit: ')
        if comm == 'use':
            dig1=float(input('Введите число: '))
            dig2 = float(input('Введите число: '))
            print('Введите название операции из доступных: ')
            showOperation()
            name = input()
            print(useOperation(dig1,dig2,name))
        elif comm == 'add':
            name = input('Введите название операции: ')
            print(addOperation(name))
        elif comm == 'show':
            showOperation()
        elif comm == 'exit':
            exit()
        else:
            print('Попробуйте еще раз')
main()


