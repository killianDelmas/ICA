import numpy as np
from scipy import linalg
from PIL import Image
import matplotlib.image as mpimag
import matplotlib.pyplot as plt
import sys
import math

afficher = False
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

A = [[0.9,0.1],[0.8,0.2]]


# Combinaison linéaire des tableaux
img3 = A[0][0] * img1 + A[0][1] * img2
img4 = A[1][0] * img1 + A[1][1]*img2

# Afficher l'image résultante
if afficher:
    fig,axes = plt.subplots(1,2)
    axes[0].imshow(img3)
    axes[1].imshow(img4)
    plt.tight_layout()
    plt.show()

tailles = img3.shape
# print(tailles)
# print(img3[:,:,0].shape)
# X1 = img3.reshape((tailles[0]*tailles[1],3))
# X2 = img4.reshape((tailles[0]*tailles[1],3))
# X2 = img4.reshape(-1)
# X = np.array([X1,X2])
# print(X.shape)

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

X1bar = sigma1*(U[0][0]*X1centre+U[0][1]*X2centre)
X2bar = sigma2*(U[1][0]*X1centre+U[1][1]*X2centre)

# Etape 3 : 

Phi1 = 1/4*math.atan(-sum(2*(X1bar**3)*X2bar-2*(X2bar**3)*X1bar)/sum(3*(X1bar**2)*(X2bar**2)-0.5*(X1bar**4)-0.5*(X2bar**4)))

V = [[math.cos(Phi1),math.sin(Phi1)],[-math.sin(Phi1),math.cos(Phi1)]]

S1 = V[0][0]*X1bar+V[0][1]*X2bar
S2 = V[1][0]*X1bar+V[1][1]*X2bar

S1 = S1- min(S1)
S1 = S1/max(S1)
S1 = S1.reshape(tailles)

S2= S2 - min(S2)
S2temp = S2/max(S2)
S2 = S2temp.reshape(tailles)

# print(S1)
plt.figure(1)
plt.imshow(S1)
plt.figure(2)
plt.imshow(S2)

plt.show()






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


# S1 = np.zeros(tailles)
# S2 = np.zeros(tailles)

# for i in range(3) :
#     X1 = img3[:,:,i].reshape((tailles[0]*tailles[1]))
#     X2 = img4[:,:,i].reshape((tailles[0]*tailles[1]))
#     X1centre = X1 - np.mean(X1)
#     X2centre = X2 - np.mean(X2)
#     print(X1centre.shape)
#     # Etape 1 : 


#     Phi0 = 0.5*math.atan(-2*sum(X1centre*X2centre)/sum(X1centre**2-X2centre**2))

#     U = [[math.cos(Phi0),math.sin(Phi0)],[-math.sin(Phi0),math.cos(Phi0)]]

#     # Etape 2 : 

#     sigma1 = sum((X1centre*math.cos(Phi0)+X2centre*math.sin(Phi0))**2)
#     sigma2 = sum((X1centre*math.cos(Phi0-math.pi/2)+X2centre*math.sin(Phi0-math.pi/2))**2)

#     X1bar = sigma1*(U[0][0]*X1centre+U[0][1]*X2centre)
#     X2bar = sigma2*(U[1][0]*X1centre+U[1][1]*X2centre)

#     # Etape 3 : 

#     Phi1 = 1/4*math.atan(-sum(2*(X1bar**3)*X2bar-2*(X2bar**3)*X1bar)/sum(3*(X1bar**2)*(X2bar**2)-0.5*(X1bar**4)-0.5*(X2bar**4)))

#     V = [[math.cos(Phi1),math.sin(Phi1)],[-math.sin(Phi1),math.cos(Phi1)]]

#     S1temp = V[0][0]*X1bar+V[0][1]*X2bar
#     S2temp = V[1][0]*X1bar+V[1][1]*X2bar

#     S1temp = S1temp - min(S1temp)
#     S1temp = S1temp/max(S1temp)
#     S1[:,:,i] = S1temp.reshape((tailles[0],tailles[1]))

#     S2temp = S2temp - min(S2temp)
#     S2temp = S2temp/max(S2temp)
#     S2[:,:,i] = S2temp.reshape((tailles[0],tailles[1]))
