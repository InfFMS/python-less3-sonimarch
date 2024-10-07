# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, сколько было введено простых натуральных чисел
# (которые делятся только сами на себя и на 1), и сколько составных.


cnt = 0
b = 0
while (a := int(input())) != 0:
    b += 1
    for i in range(2, int((a ** 0.5) // 1 + 1)):
        if a % i == 0:
            break
    else:
        cnt += 1

print(f'Простых чисел: {cnt} и Составных чисел: {b - cnt}')