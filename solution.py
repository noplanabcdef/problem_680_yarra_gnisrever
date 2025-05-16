def fast_doubling(n, mod):
    if n == 0:
        return (0, 1)
    a, b = fast_doubling(n // 2, mod)
    c = a * (2 * b - a) % mod
    d = (a * a + b * b) % mod
    if n % 2 == 0:
        return (c, d)
    else:
        return (d, (c + d) % mod)
