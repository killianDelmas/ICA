import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import math
import Whitening as wt

# Applique une méthode ICA
def ICA(X1,X2):

    X1centre = X1 - np.mean(X1)
    X2centre = X2 - np.mean(X2)

    # Etape 1 : Rotation 1

    Phi0 = 0.5*math.atan(-2*sum(X1centre*X2centre)/sum(X1centre**2-X2centre**2))

    U = [[math.cos(Phi0),math.sin(Phi0)],[-math.sin(Phi0),math.cos(Phi0)]]

    # Etape 2 : Déaplanissement

    sigma1 = sum((X1centre*math.cos(Phi0)+X2centre*math.sin(Phi0))**2)
    sigma2 = sum((X1centre*math.cos(Phi0-math.pi/2)+X2centre*math.sin(Phi0-math.pi/2))**2)

    X1bar = (U[0][0]*X1centre+U[0][1]*X2centre)/math.sqrt(sigma1)
    X2bar = (U[1][0]*X1centre+U[1][1]*X2centre)/math.sqrt(sigma2)

    # Etape 3 : Rotation 2

    Phi1 = 1/4*math.atan(-sum(2*(X1bar**3)*X2bar-2*(X2bar**3)*X1bar)/sum(3*(X1bar**2)*(X2bar**2)-0.5*(X1bar**4)-0.5*(X2bar**4)))

    V = [[math.cos(Phi1),math.sin(Phi1)],[-math.sin(Phi1),math.cos(Phi1)]]

    S1 = V[0][0]*X1bar+V[0][1]*X2bar
    S2 = V[1][0]*X1bar+V[1][1]*X2bar

    return S1,S2




