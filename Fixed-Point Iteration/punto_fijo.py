import numpy as np

def cached_punto_fijo(g, P0, TOL, No):
    i = 1
    P0 = P0
    cache = []
    while i <= No:
        P = g(P0)
        cache.append([i, P0, P])
        if abs(P - P0) < TOL:
            return P,cache
        P0 = P
        i += 1
        

    return "El método falló después de No iteraciones, No ={}".format(str(No)),cache

