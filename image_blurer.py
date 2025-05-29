import numpy as np
import cv2
import matplotlib.pyplot as plt

img=cv2.imread("poster2.png")
img2=img.copy()


if(img.shape[0]>600):

    resize_power=img.shape[0]//600
    width = int(img.shape[1] * resize_power / 100)
    height = int(img.shape[0] * resize_power / 100)
    dim = (width, height)

# Resize image
    img2 = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    img=img2.copy()

#use convulation type
convu_mat= np.array([[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]])

def get_new_pixel(i,j,img,pixel_range):
    ans=0.0
    pix=pixel_range//2
    for ii in range(-pix,pix+1):
        for jj in range(-pix,pix+1):
            ans = ans + img[i+ii,j+jj]

    ans = ans/(pixel_range*pixel_range)
    return ans
pixel_range=img.shape[0]//33
start_pixel=pixel_range//2

for i in range(start_pixel,img2.shape[0]-start_pixel):
    for j in range(start_pixel,img.shape[1]-start_pixel):
        img2[i,j]=get_new_pixel(i,j,img2,pixel_range)
    if(img2.shape[0]//i==2 and img2.shape[1]//j==2):
        print(f"Half way thorugh {i} pixels")




plt.title(f"Image before {pixel_range}^2 matrix convulation")
plt.imshow(img)

plt.title(f"Image after {pixel_range}^2 matrix convulation")
plt.imshow(img2)


