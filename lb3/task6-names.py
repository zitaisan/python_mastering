def checkDuplicates(usernames):
    unique_names = set()
    duplicates = set()
    for name in usernames:
        if name in unique_names:
            duplicates.add(name)
        else:
            unique_names.add(name)
    if duplicates:
        print("Найдены повторяющиеся имена:", ", ".join(duplicates))
    else:
        print("Дубликатов не найдено.")


def removeDuplicates(usernames):
    return list(set(usernames))


def main():
    while True:
        user_input = input("Введите имена пользователей через запятую или 'stop' для выхода: ")
        if user_input.lower() == 'exit':
            exit()
        usernames = [name.strip() for name in user_input.split(",")]
        checkDuplicates(usernames)
        unique_usernames = removeDuplicates(usernames)
        print("Список без дубликатов:", unique_usernames)
main()
