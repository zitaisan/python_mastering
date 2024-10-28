x = input("Введите строку ")
res = ""
for char in x:
    if char.isalpha():
        if char == 'z':
            res += 'a'
        elif char == 'Z':
            res += 'A'
        else:
            res += chr(ord(char) + 1)
    else:
        res += char
print(res)