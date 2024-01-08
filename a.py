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
