import os
FILENAME = "input.txt"
OUTFILE = "out.txt"
def reverse():
    with open(FILENAME, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        lines = [line if line.endswith('\n') else line + '\n' for line in lines]

        reversed_lines = reversed(lines)
        with open(OUTFILE, 'w', encoding='utf-8') as outfile:
            outfile.writelines(reversed_lines)
    print(f"Файл '{outfile}' успешно создан")

def main():
    reverse()
main()
