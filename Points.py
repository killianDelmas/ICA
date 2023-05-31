import sys
import numpy as np
import matplotlib.image as mpimag
import matplotlib.pyplot as plt
import ICA as ica
import Whitening as wt

arguments = sys.argv
whitening = True
if len(arguments) > 1 :
    if(arguments[1] == "false"):
        whitening = False


n=200

# Paramètres de la droite
A = 2
b = -10

# Générer les coordonnées x
x = np.linspace(0, 10, n)


# Générer les coordonnées y1 et y2
y1 = A * x + b
y2 = -A * x - b

noise1 = np.random.normal(0, 1, len(x))
noise2 = np.random.normal(0, 1, len(x))

y1 = y1 + noise1
y2 = y2 + noise2


plt.subplot(1,3,1)
plt.plot(x, y1, 'r+',x,y2,'b+')
plt.title("Donnée Initial")
plt.axis('off')

# Mélange les signaux
A = [[0.6,0.4],[0.4,0.6]]
X1 = A[0][0] * y1 + A[0][1] * y2
X2 = A[1][0] * y1 + A[1][1]* y2

plt.subplot(1,3,2)
plt.plot(x, X1, 'r+',x,X2,'b+')
plt.title("Donnée Mélangée")

# Whitening des données si demandé
if whitening :
    X1,X2,V,Dinv = wt.Whitening(X1,X2)

# Applique l'ICA
S1,S2 = ica.ICA(X1,X2)

plt.subplot(1,3,3)
plt.plot(x, S1, 'r+',x,S2,'b+')
plt.title("Donnée retrouvée")


plt.show()
