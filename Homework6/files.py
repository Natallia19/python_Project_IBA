# Вариант 2
# Скопировать в файл F2 только те строки из F1, которые начинаются с буквы «А».

f1 = open("f1.txt", "r")
f2 = open("f2.txt", "w")

lst = []
a_lst = []

for s in f1:
    s = s.lstrip()
    lst = lst + [s]

# если строка начинается с буквы А(а), добавляем ее в новый список
for s in lst:
    if s.startswith('A') == True or s.startswith('a') == True:
        a_lst.append(s)
print(*a_lst, sep='\n')

# записываем список в файл f2
for s in a_lst:
    f2.write(s)

f1.close()
f2.close()
