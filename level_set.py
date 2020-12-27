import numpy as np
import scipy.ndimage
import scipy.signal
import matplotlib.pyplot as plt
from skimage import color, io
from skimage.transform import resize
import sys
np.set_printoptions(threshold=sys.maxsize)


def grad(x): #đạo hàm
    return np.array(np.gradient(x))


def norm(x, axis=0):
    return np.sqrt(np.sum(np.square(x), axis=axis))


def stopping_fun(x):
    return 1. / (1. + norm(grad(x))**2)


def default_phi(x):#init area
    # Initialize surface phi at the border (5px from the border) of the image
    # i.e. 1 outside the curve, and -1 inside the curve
    phi = np.ones(x.shape[:2])# tạo matrix height*width toàn 1 
    phi[105:120, 60:70] = -1. #vùng ban đầu, x and y lộn ngược, =-1 là ở trong contour
    return phi


def stopping_fun(x, alpha):
    return 1. / (1. + alpha * norm(grad(x))**2)

def curvature(f):
    fy, fx = grad(f)
    norm = np.sqrt(fx**2 + fy**2)
    Nx = fx / (norm + 1e-8)
    Ny = fy / (norm + 1e-8)
    return div(Nx, Ny)


def div(fx, fy):
    fyy, fyx = grad(fy)
    fxy, fxx = grad(fx)
    return fxx + fyy


def dot(x, y, axis=0):
    return np.sum(x * y, axis=axis)

v = 1.
dt = 1.
img = io.imread('Liver_MRI0001/phase1/img0059.dcm')
img = color.rgb2gray(img)#data của thư viện, ko bik chứa gì, 1 cái matrix
img = img - np.mean(img)
img_smooth = scipy.ndimage.filters.gaussian_filter(img, 3)
F = stopping_fun(img_smooth, 0.5)
phi = default_phi(img_smooth) #đánh dấu

for i in range(1000):
    dphi = grad(phi)
    dphi_norm = norm(dphi)
    kappa = curvature(phi)


    dphi_t = -F * dphi_norm

    phi = phi + dt * dphi_t

plt.imshow(img, cmap='Greys_r')
plt.contour(phi, 0, colors='r', linewidths=[3])
plt.draw()
plt.show()
                
