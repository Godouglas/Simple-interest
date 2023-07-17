def i(p, r, t):
    print(p * r * t * 0.01)


def p(i, r, t):
    print((100 * i) / (r*t))


def r(i, p, t):
    print((100 * i) / (p * t))


def t(r, i, p):
    print((100 * i) / (p * r))
