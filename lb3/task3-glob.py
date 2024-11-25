
counter = 0


def callCounter():
    global counter
    counter += 1
    print(f"Количество вызовов: {counter}")


def resetCounter():
    global counter
    counter = 0
    print("Счетчик сброшен")


def main():
    while True:
        comm = input(
            "Введите команду call, reset, exit: ")

        if comm == "call":
            callCounter()
        elif comm == "reset":
            resetCounter()
        elif comm == "exit":
            comm = input(
                "Вы точно хотите выйти??? напишите 'no' ")
            if comm !='no':
                exit()
        else:
            print("Попробуйте еще раз")

main()
