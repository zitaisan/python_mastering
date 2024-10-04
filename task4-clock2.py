n = int(input("Введите n: "))
days = n // 60 // 24 // 60
hours = (n - 60 * 60 * (days * 24)) // 60 // 60
minutes = (n - 60 * hours * 60 - 24 * 60 * days * 60) // 60
seconds = (n - 60 * hours * 60 - 24 * 60 * days * 60 - 60 * minutes)
print(str(hours).zfill(2), str(minutes).zfill(2), str(seconds).zfill(2), sep=":")
