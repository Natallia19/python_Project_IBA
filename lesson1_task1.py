# вариант 5.Определить, есть ли среди заданных целых чисел
# A, B, C, D хотя бы одно нечётное.

while True:
    print("Введите 4 целых числа: ")
    a, b, c, d = int(input()), int(input()), int(input()), int(input())

    if a %2==0 or b %2==0 or c %2==0 or d %2==0:
        print("среди заданных целых чисел ЕСТЬ четное число")
    else:
        print("среди заданных целых чисел НЕТ четного числа")
    if input('Do You Want To Continue? ') != 'y':
        break