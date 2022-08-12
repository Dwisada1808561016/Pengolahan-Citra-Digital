import cv2
import numpy as np
from matplotlib import pyplot as plt


test_image = cv2.imread('rose.png',0) #gambar dibaca grayscale

#cv2.Sobel(original_image,ddepth,xorder,yorder,kernelsize)
#tanda cv2.CV_64F adalah format grayscale 64 bit (true color)
#sedangkan cv2.CV_8U adalah format binary atau 8 bit (hitam putih)
sobelx = cv2.Sobel(test_image,cv2.CV_64F,1,0,ksize=3)
sobely = cv2.Sobel(test_image,cv2.CV_64F,0,1,ksize=3)

plt.figure()
plt.subplot(1,2,1),plt.imshow(sobelx,cmap='gray'),plt.title('Penerapan Sobel X')
plt.subplot(1,2,2),plt.imshow(sobely,cmap='gray'),plt.title('Penerapan Sobel Y')



G = np.sqrt(sobely**2+sobelx**2)
theta = np.arctan2(sobely, sobelx)

plt.figure()
plt.imshow(np.uint8(G),cmap='gray')
plt.title('Penerapan Sobel ')
