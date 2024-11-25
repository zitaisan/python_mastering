import os
FILENAME = "tasks.txt"
def search(word):
    with open(FILENAME, 'r', encoding='utf-8') as file:
        count = 0
        lines= []

        for line_number, line in enumerate(file, start=1):
                # Настраиваем поиск с учетом игнорирования регистра
            matches = line.lower().count(word.lower())
            if matches > 0:
                count += matches
                lines.append((line_number, line.strip()))
    return count, lines


def main():
    word = input("Введите слово для поиска: ").strip()
    count, lines = search(word)
    if count > 0:
        print(f"\nСлово '{word}' найдено {count} раз(а).")
        print("\nСтроки, содержащие слово:")
        for line_number, line in lines:
            print(f"{line_number}: {line}")
    else:
        print(f"\nСлово '{word}' не найдено.")


main()
