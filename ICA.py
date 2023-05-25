import numpy as np
from scipy import linalg
import matplotlib.image as mpimag


X = [[2,3],[1,1]]

X = np.array(X)

# On centre les données

#Calcul de Xmean
Xmean = np.mean(X,0)
#Calcul de Xcentre
Xcentre = X - Xmean


Xcov = np.cov(Xcentre, rowvar=True, bias=True)

w, V = linalg.eig(Xcov)

D = np.diag(1/((w+.1e-5)**0.5))

D = D.real.round(4)

Xpret = (V@D)@(V.T@Xcentre)


