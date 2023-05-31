import numpy as np
import numpy as np
from scipy import linalg
from PIL import Image
import matplotlib.image as mpimag
import matplotlib.pyplot as plt
import sys
import math
import ICA as ica
import Whitening as wt

n=200

# Paramètres de la droite
A = 2
b = -10

# Générer les coordonnées x
x = np.linspace(0, 10, n)


# Générer les coordonnées y
y1 = A * x + b
y2 = -A * x - b

# Générer un bruit aléatoire pour les coordonnées y
noise1 = np.random.normal(0, 1, len(x))
noise2 = np.random.normal(0, 1, len(x))
# Ajouter du bruit aux coordonnées y
y1 = y1 + noise1
y2 = y2 + noise2

plt.figure(1)

plt.plot(x, y1, 'r+',x,y2,'b+')

A = [[0.6,0.4],[0.4,0.6]]
X1 = A[0][0] * y1 + A[0][1] * y2
X2 = A[1][0] * y1 + A[1][1]* y2

plt.figure(2)
plt.plot(x, X1, 'r+',x,X2,'b+')

X1,X2 = wt.Whitening(X1,X2)


# X1 = [y1[i] if i%2==0 else y2[i] for i in range(len(y1)) ]
# X2 = [y2[i] if i%2==0 else y1[i] for i in range(len(y2)) ]


S1,S2 = ica.ICA(X1,X2)

plt.figure(3)
plt.plot(x, S1, 'r+',x,S2,'b+')

plt.show()
