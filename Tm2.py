#fib(n)
1,1,2,3,5,8,13,
#fib(n) = fib(n-1) + fib(n-2)
#shart bazgasht :
#if (n = 1) or (n = 2) :
#meqdar bazgasht :
#1
def fibonacci_naive(n):
    if n <= 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)


def multiply_matrices_simple(a, b):
    n = len(a)
    m = len(a[0])
    p = len(b[0])

    c = [[0 for _ in range(p)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            for k in range(p):
                c[i][k] = c[i][k] + a[i][j] * b[j][k]

    return c


def strange_rec(a, b):
    if a <= 0 or b <= 0:
        return 0
    if a > b:
        return a * b
    return strange_rec(a, b - 2) + strange_rec(a - 1, b - 3) + 6


# نمونه اجرا
print(fibonacci_naive(7))      # 13
print(strange_rec(3, 7))       # 45
    