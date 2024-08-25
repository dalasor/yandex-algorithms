from sympy import Symbol, simplify, binomial

n = Symbol('n')
B1A0 = (1 / n) * binomial(48, n - 1) / binomial(51, n - 1)
B2A1 = (2 / n) * binomial(3, 1) * binomial(49, n - 2) / binomial(51, n - 1)
B3A2 = (3 / n) * binomial(3, 2) * binomial(50, n - 3) / binomial(51, n - 1)
B4A3 = (4 / n) * binomial(51, n - 4) / binomial(51, n - 1)
print(simplify(B1A0 + B2A1 + B3A2 + B4A3))
