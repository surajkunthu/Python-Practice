def deriv(f, a):
    h = 0.000001
    dy = f(a+h) - f(a)
    dx = h
    return dy/dx

def h(x):
    return x**2

def g(x):
    return x**4 - x**(1/2)


#TESTS
h(3)
deriv(h, 2)
deriv(h, 8)
deriv(g, 4)
deriv(g, 2.71)
