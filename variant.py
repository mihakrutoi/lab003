number = int(input("Введите целое число от 0 до 100: "))

if number < 0 or number > 100:
    print("Ошибка диапазона")
else:
    if 0 <= number <= 30:
        print("Категория 1")
    elif 31 <= number <= 70:
        print("Категория 2")
    else:
        print("Категория 3")