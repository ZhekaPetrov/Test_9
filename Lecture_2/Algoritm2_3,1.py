#Дана последовательность чисел длинной N (N > 0)
#Найти максимальное число в последовательности.
def max_num(N):
    ans = 0
    for i in range(len(N)):
        if N[i] > ans:
            ans = N[i]
    return ans


result = max_num([1, 3, 4, 23, 45, 9])
print(f"Максимально число: {result}")