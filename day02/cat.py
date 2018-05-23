
from scipy.misc import imread
import numpy as np
import pylab
import matplotlib.pyplot as plt
im = imread('/Users/ljf/Desktop/tree.png')
R = im[:,:,0]
G = im[:,:,1]
B = im[:,:,2]

R= (R & 3) * 85
G= (G & 3) * 85
B= (B & 3) * 85

new_img = np.array([R,G,B])
print(new_img)
imshow(new_img)