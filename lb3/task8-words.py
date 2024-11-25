def countUnique(text):
    words = set(text.lower().split())
    return len(words)

def main():
    while True:
        text = input("Введите текст (или 'exit' для выхода): ")
        if text.lower() == 'exit':
            exit()
        unique_count = countUnique(text)
        print(f"Количество уникальных слов: {unique_count}")

main()
