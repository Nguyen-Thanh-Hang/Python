n = int(input('Nhập n = '))
def fibonacci(n):
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        first, second = 0, 1
        for i in range(2, n+1):
            first, second = second, first + second
            return second
result = fibonacci(n)
print('Số fibonacci thứ', n, 'là', result)