import numpy as np

def newton(f, df, p0, TOL, N0):
    p0 = p0
    i = 1
    while i <= N0:
        p = p0 - f(p0)/df(p0)
        if abs(p-p0) < TOL:
            return p
        p0 = p
        i += 1

    return "El método falló despues de N0 iteraciones, N0 = {}".format(str(N0))

def newton_cached(f, df, p0, TOL, N0):
    print("Aproximacion inicial p0 = ", p0)
    print("Numero de iteraciones N0 = ", N0)
    p0 = p0
    i = 1
    cache = []
    while i <= N0:
        cache.append([i, p0])
        p = p0 - f(p0)/df(p0)
        if abs(p-p0) < TOL:
            return p, cache
        p0 = p
        i += 1

    return "El método falló despues de N0 iteraciones, N0 = {}".format(str(N0)), cache
  
