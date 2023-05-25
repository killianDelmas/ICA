import numpy as np
from scipy import linalg
from PIL import Image
import matplotlib.image as mpimag
import matplotlib.pyplot as plt
import sys

afficher = False
arguments = sys.argv
if len(arguments) > 2 :
    img = Image.open(arguments[1])
    new_img = img.resize((480,256))
    new_img.save('Image1.png','png')
    imag2 = Image.open(arguments[2])
    nimg2 = imag2.resize((480,256))
    nimg2.save('Image2.png','png')

image1 = plt.imread('Image1.png')
image2 = plt.imread('Image2.png')

img1 = np.array(image1)
img2 = np.array(image2)

# Combinaison linéaire des tableaux
img3 = 0.7 * img1 + 0.3 * img2
img4 = 0.4 * img1 + 0.6*img2

# Afficher l'image résultante
if afficher:
    fig,axes = plt.subplots(1,2)
    axes[0].imshow(img3)
    axes[1].imshow(img4)
    plt.tight_layout()
    plt.show()

tailles = img3.shape

X1 = img3.reshape(-1)
X2 = img4.reshape(-1)
X = np.array([X1,X2])
print(X.shape)


# X = np.array(X)

# # On centre les données

# #Calcul de Xmean
# Xmean = np.mean(X,0)
# #Calcul de Xcentre
# Xcentre = X - Xmean


# Xcov = np.cov(Xcentre, rowvar=True, bias=True)

# w, V = linalg.eig(Xcov)

# D = np.diag(1/((w+.1e-5)**0.5))

# D = D.real.round(4)

# Xpret = (V@D)@(V.T@Xcentre)


