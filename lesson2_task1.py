# Вариант 5
# 1.Найдите наименьший четный элемент списка. Если такого нет, то выведите первый элемент.
# 2.Преобразовать список так, чтобы сначала шли нулевые элементы, а затем все остальные.

numbersList = [int(i) for i in input('Enter values separated by enter ').split()]
#displaying the original list
print(numbersList)
#sort the list in ASC order
numbersList.sort()
#sorted list output
print(numbersList)

print("Min even number: ")

for i in numbersList:
    if i % 2 == 0 and i != 0:
         print(i)
         break