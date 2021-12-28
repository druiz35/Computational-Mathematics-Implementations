import numpy as np

def binary_search(function, a, b, N_o, TOL):
    FA = function(a)
    ai, bi = a, b
    print("INTERVALO = [{},{}]".format(str(a), str(b)))
    print("No = {}".format(str(N_o)))
    for i in range(N_o):
        p = ai + (bi-ai)/2
        FP = function(p)
        if FP == 0 or (bi-ai)/2 < TOL:
            return p
        if FA*FP>0:
            FA = FP
            ai = p
        else:
            bi = p
    return "The method failed after N_o iterations, with N_o = {}".format(str(N_o))

def cached_binary_search(function, a,b,No, TOL):
    i = 1
    FA = function(a) 
    print("INTERVALO = [{},{}]".format(str(a), str(b)))
    print("No = {}".format(str(No)))
    cache = []
    ai, bi, = a,b
    while i <= No:
        p = ai+(bi-ai)/2
        FP = function(p)
        cache.append([i, ai, p, bi, FP])
        if FP == 0 or (bi-ai)/2 < TOL:
            return p, cache
        if FA*FP>0:
            FA = FP
            ai = p
        else:
            bi = p
        i += 1
    return "The method failed after No iterations, with No = {}".format(str(No)), cache


