# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить минимальное из введённых чисел Фибоначчи.
# Вывести "нет", если чисел Фибоначчи в последовательности нет.
# Числа Фибоначчи – это последовательность чисел,
# которая начинается с двух единиц и каждое следующее число
# равно сумме двух предыдущих: 1, 1, 2, 3, 5, 8, 13, …


s = []
d = []
while (a := int(input())) != 0:
    s.append(a)
if s:
    s.sort()
    i = 0
    a = b = 1
    while b <= max(s):
        d.append(a)
        d.append(b)
        b += a
        a += b
    for i in s:
        if i in d:
            print(f'Минимальное число Фибоначчи: {i}')
            break
    else:
        print('нет')
else:
    print('нет')