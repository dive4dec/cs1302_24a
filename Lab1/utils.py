def f(n):
    if n > 0:
        return n ** f(n - 1)
    return 1