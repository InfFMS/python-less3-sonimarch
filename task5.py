# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, среднее арифметическое тех введённых чисел,
# которые являются степенями числа 2.
# Вывести "нет", если таких чисел нет.

s = 0
cnt = 0

while (a := int(input())) != 0:
    n = a
    if a == 1:
        f = False
    while a > 1:
        if a % 2 == 0:
            a //= 2
            f = True
        else:
            f = False
            break
    if f:
        s += n
        cnt += 1
print(f'Среднее арифметическое чисел, являющихся степенями двойки: {round(s / cnt, 2)}' if cnt != 0 else 'нет')