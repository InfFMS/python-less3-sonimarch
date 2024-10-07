# с клавиатуры вводится число N, а затем – N натуральных чисел.
# Определить минимальное и максимальное среди простых чисел
# (которые делятся на сами не себя и на 1).
# Если таких чисел не было, вывести "нет".


s = []
for j in range(int(input())):
    a = int(input())
    if a == 1:
        continue
    for i in range(2, int((a ** 0.5) // 1 + 1)):
        if a % i == 0:
            break
    else:
        s.append(a)
if s:
    print(min(s), max(s))
else:
    print('нет')