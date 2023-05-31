import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import sys
import math
from scipy import linalg

def Whitening(X1,X2):

    X = [X1,X2]
    print(X)

    #Calcul de Xmean
    Xmean = np.mean(X,0)
    #Calcul de Xcentre
    Xcentre = X - Xmean


    Xcov = np.cov(Xcentre, rowvar=True, bias=True)

    w, V = linalg.eig(Xcov)

    D = np.diag(1/((w+.1e-5)**0.5))

    D = D.real.round(4)

    Xpret = (V@D)@(V.T@Xcentre)

    return Xpret[0],Xpret[1]
