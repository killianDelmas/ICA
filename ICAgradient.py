import math
import numpy as np
from scipy import linalg

# Applique l'ICA en utilisant une méthode de gradient
def gradiantICA(X1,X2):
    
    # Initialisation des paramètres
    n = 2
    N = len(X1)
    W = np.eye(n)
    X = np.array([X1,X2])
    X = X.T
    u = X@W
    maxiter = 100
    eta = 0.25
    hs = np.zeros(maxiter)
    gs = np.zeros(maxiter)

    # Iteration
    for iter in range(maxiter):
        u=X@W
        U = np.tanh(u)
        detW = np.abs(linalg.det(W))
        h = ((1/N)*sum(sum(U))+0.5*math.log(detW))
        g = linalg.inv(W.T) - (2/N)*X.T@U
        W = W + eta*g
        hs[iter] = h
        gs[iter] = linalg.norm(g)
    S = U.T
    return S,hs,gs
        