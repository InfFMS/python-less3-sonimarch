# с клавиатуры вводится число N, а затем – N целых чисел.
# Определить, сколько было введено положительных и
# сколько отрицательных чисел (нули не считать!).


s = [int(input()) for i in range(int(input()))]
print(sum([1 if i > 0 else 0 for i in s]))
print(sum([1 if i < 0 else 0 for i in s]))