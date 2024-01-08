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

fib = [0] * (4)
fib

# %%
