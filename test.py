import numpy as np
import numpy as np
from scipy import linalg
from PIL import Image
import matplotlib.image as mpimag
import matplotlib.pyplot as plt
import sys
import math

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
plt.plot(x, y1, 'r+',x,y2,'b+')
plt.show()