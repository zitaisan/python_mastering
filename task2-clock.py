n = int(input("Введите n: "))
days = n // 60 // 24
hours = (n - 60 * (days * 24)) // 60
minutes = n - 60 * hours - 24 * 60 * days
print(str(hours).zfill(2), str(minutes).zfill(2), sep=":")
