def dim(M):
    return (len(M), len(M[0]))

def produit(M1, M2):
    dimM1 = dim(M1)
    dimM2 = dim(M2)
    M3 = [[0] * dim(M2)[1] for _ in range()]
