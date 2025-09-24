import sys


def factorial_five(n):
    fact = 1
    MOD = 10 ** 12

    for i in range(1, n + 1):

        fact *= i

        while fact % 10 == 0:
            fact //= 10
        fact %= MOD
    result = fact % 100000
    return f"{result:05d}"


N = int(sys.stdin.readline())

print(factorial_five(N))

