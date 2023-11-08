#Semih Karakuş
#02195076064
#İkinci Öğretim

import cv2
import numpy as np
from matplotlib import pyplot as plt

gri = cv2.imread("Logo.png",0)
cv2.imshow("Gri",gri)
cv2.waitKey()

histogram = np.zeros(256)
[w,h] = np.shape(gri)
for yukseklik in range (0, h):
    for genislik in range (0, w):
        i= gri[genislik,yukseklik]
        histogram[i]=histogram[i]+1

plt.plot(histogram)
plt.show()