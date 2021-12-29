import numpy as np

def regula_falsi(f, p0, p1, TOL, N0):
    p0 = p0
    p1 = p1
    q0 = f(p0)
    q1 = f(p1)
    i = 2
    while i <= N0:
        p = p1 - q1*(p1-p0)/(q1-q0)
        if abs(p - p1) < TOL:
            return p
        i += 1
        q = f(p)
        if q * q1 < 0:
            p0 = p1
            q0 = q1
        p1 = p
        q1 = q
    return "The method failed after N0 iterations, N0 = {}".format(str(N0))
