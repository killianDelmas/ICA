import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import sys
import math
from scipy import linalg

# Applique le Whitening sur nos données
def Whitening(X1,X2):

    X = [X1,X2]

    #Calcul de Xmean
    Xmean = np.mean(X,0)
    #Calcul de Xcentre
    Xcentre = X - Xmean


    Xcov = np.cov(Xcentre, rowvar=True, bias=True)

    w, V = linalg.eig(Xcov)

    Dinv = np.diag((w)**0.5)
    Dinv = Dinv.real.round(4)

    D = np.diag(1/((w+.1e-5)**0.5))
    D = D.real.round(4)

    Xpret = (V@D)@(V.T@Xcentre)

    return Xpret[0],Xpret[1],V,Dinv

# Dewhitening : Sert à avoir une Image lisible
def dewhitening(S1,S2,V,Dinv) :

    S = [S1,S2]

    Sdw = V@Dinv@V.T@S

    return Sdw[0],Sdw[1]
