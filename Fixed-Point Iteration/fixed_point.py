import numpy as np

def cached_fixed_point(g, P0, TOL, No):
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
        

    return "The method failed after N0 iterations, N0 = {}".format(str(No)),cache

