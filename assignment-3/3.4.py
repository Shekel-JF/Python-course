import functools

def pamiec(func):
    dict = {}
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if(args in dict):
            return dict[args]
        else:
            fib = func(*args, **kwargs)
            dict[args] = fib
            return fib
    return wrapper


@pamiec
def fibonacci(n):
    return n if 0 <= n < 2 else fibonacci(n - 1) + fibonacci(n - 2)

for i in range(100):
    print(fibonacci(i))