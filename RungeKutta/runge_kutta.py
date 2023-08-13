def dydx(x, y, function):
    return eval(function)

def rungeKutta(x0, y0, x, h, function):
    n = (int)((x - x0) / h)
    y = y0
    for i in range(1, n + 1):
        k1 = h * dydx(x0, y, function)
        k2 = h * dydx(x0 + 0.5 * h, y + 0.5 * k1, function)
        k3 = h * dydx(x0 + 0.5 * h, y + 0.5 * k2, function)
        k4 = h * dydx(x0 + h, y + k3, function)

        y = y + (1.0 / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)

        x0 = x0 + h
    return [y, n]
