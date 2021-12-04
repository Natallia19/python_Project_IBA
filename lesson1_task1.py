# вариант 5.Определить, есть ли среди заданных целых чисел
# A, B, C, D хотя бы одно нечётное.

while True:
    print("Введите 4 целых числа: ")
    a, b, c, d = int(input()), int(input()), int(input()), int(input())

    a %= 2
    b %= 2
    c %= 2
    d %= 2

    if a == b and b == c and c == d and d == a:
        print("среди заданных целых чисел НЕТ четного числа")
    else:
        print("среди заданных целых чисел ЕСТЬ четное число")
    if input('Do You Want To Continue? ') != 'y':
        break