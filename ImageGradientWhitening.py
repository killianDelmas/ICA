import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import sys
import math
import ICA as ica
import Whitening as wt
import ICAgradient as fa

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

A = [[0.6,0.4],[0.4,0.6]]
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

X1,X2,V,Dinv = wt.Whitening(X1,X2)

S,hs,gs = fa.gradiantICA(X1,X2)
S1 = S[0]
S2 = S[1]

S1,S2 = wt.dewhitening(S1,S2,V,Dinv)
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