# с клавиатуры вводится число N, а затем – N целых чисел.
# Определить минимальное и максимальное среди двузначных чисел,
# которые делятся на 3. Если таких чисел не было, вывести "нет".

s = [a if len(a := input()) == 2 and int(a) % 3 == 0 else 0 for i in range(int(input()))]
s = set(s)
s.discard(0)
if s:
    print(min(s))
    print(max(s))
else:
    print('нет')