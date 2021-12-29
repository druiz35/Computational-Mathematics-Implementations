import numpy as np


def secant(f, p0, p1, TOL, N0):
    q0 = f(p0)
    q1 = f(p1)
    i = 2
    p0 = p0
    p1 = p1
    while i <= N0:
        p = p1 - q1*(p1-p0)/(q1-q0)
        print(i-2, p0, p1, p, f(p))
        print("\n")
        if abs(p-p1) < TOL:
            return p
        i += 1
        p0 = p1
        p1 = p
        q0 = q1
        q1 = f(p)

