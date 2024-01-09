# %%
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


fib_10 = fibonacci(10)
fib_10

# %%
# dynamic programming for Fibnacci numbers


def fibonacci(n):
    # good for direct access fib[n]
    fib = [0] * (n+1)
    fib[0] = 0
    if n > 0:
        fib[1] = 1
        # from 2 to `n-1`
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]


fib_20 = fibonacci(20)
fib_20
# %%
# cutting rod dyanmic programming problems
# the rod can cut up to length `n` to 2^n-1 differnet ways
# p = price, n = length, q = max price


def cut_rod(p, n):
    if n == 0:
        return 0
    q = - float('inf')  # negative infinity

    for i in range(1, n+1):
        q = max(q, p[i] + cut_rod(p, n-i))
    return q


t = cut_rod([0] * 40, 40)
t  # no good, take too long to run,
# %%


def cut_rod_dp(prices, n):
    revenue = [0] * (n+1)
    for j in range(1, n+1):
        max_val = - float('inf')
        for i in range(1, j+1):
            max_val = max(max_val, prices[i] + revenue[j-i])
        revenue[j] = max_val
    return revenue[n]


# example to use it
prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]  # same as book
max_rev = cut_rod_dp(prices, 4)

print(max_rev)

# %%
