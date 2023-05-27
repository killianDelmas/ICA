import numpy as np
from scipy import linalg
from PIL import Image
import matplotlib.image as mpimag
import matplotlib.pyplot as plt
import sys
import math

arguments = sys.argv
size = (480,256)

if len(arguments) > 2 :
    img = Image.open(arguments[1])
    new_img = img.resize(size)
    new_img.save('Image1.png','png')
    imag2 = Image.open(arguments[2])
    nimg2 = imag2.resize(size)
    nimg2.save('Image2.png','png')

image1 = plt.imread('Image1.png')
image2 = plt.imread('Image2.png')

img1 = np.array(image1)
img2 = np.array(image2)

plt.subplot(3,2,1)
plt.imshow(img1)
plt.title("Image d'origine 1")
plt.axis('off')
plt.subplot(3,2,2)
plt.imshow(img2)
plt.title("Image d'origine 2")
plt.axis('off')

# Combinaison linéaire des tableaux

A = [[0.5,0.5],[0.4,0.6]]
img3 = A[0][0] * img1 + A[0][1] * img2
img4 = A[1][0] * img1 + A[1][1]*img2

# Afficher l'image résultante
plt.subplot(3,2,3)
plt.imshow(img3)
plt.title('Image mélangée 1')
plt.axis('off')
plt.subplot(3,2,4)
plt.imshow(img4)
plt.title('Image mélangée 2')
plt.axis('off')
    

tailles = img3.shape

X1 = img3.reshape(-1)
X2 = img4.reshape(-1)
X1centre = X1 - np.mean(X1)
X2centre = X2 - np.mean(X2)

# Etape 1 : 


Phi0 = 0.5*math.atan(-2*sum(X1centre*X2centre)/sum(X1centre**2-X2centre**2))

U = [[math.cos(Phi0),math.sin(Phi0)],[-math.sin(Phi0),math.cos(Phi0)]]

# Etape 2 : 

sigma1 = sum((X1centre*math.cos(Phi0)+X2centre*math.sin(Phi0))**2)
sigma2 = sum((X1centre*math.cos(Phi0-math.pi/2)+X2centre*math.sin(Phi0-math.pi/2))**2)

X1bar = (U[0][0]*X1centre+U[0][1]*X2centre)/math.sqrt(sigma1)
X2bar = (U[1][0]*X1centre+U[1][1]*X2centre)/math.sqrt(sigma2)

# Etape 3 : 

Phi1 = 1/4*math.atan(-sum(2*(X1bar**3)*X2bar-2*(X2bar**3)*X1bar)/sum(3*(X1bar**2)*(X2bar**2)-0.5*(X1bar**4)-0.5*(X2bar**4)))

V = [[math.cos(Phi1),math.sin(Phi1)],[-math.sin(Phi1),math.cos(Phi1)]]

S1 = V[0][0]*X1bar+V[0][1]*X2bar
S2 = V[1][0]*X1bar+V[1][1]*X2bar

S1 = S1- min(S1)
S1 = S1/max(S1)
S1 = S1.reshape(tailles)

S2= S2 - min(S2)
S2 = S2/max(S2)
S2 = S2.reshape(tailles)


plt.subplot(3,2,5)
plt.imshow(S1)
plt.title("Image reconstruite 1")
plt.axis('off')
plt.subplot(3,2,6)
plt.imshow(S2)
plt.title("Image reconstruite 2")
plt.axis('off')

plt.show()

