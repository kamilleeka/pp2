def simpsons_rule(f, a, b, n):
    h = (b-a)/n
    s = f(a) + f(b)
    for i in range(1, n, 2):
        s += 4 * f(a + i * h)
    for i in range(2, n-1, 2):
        s += 2 * f(a + i * h)
    return (h/3) * s