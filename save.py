#import cv2
import numpy as np
from matplotlib import pyplot as plt
import numpy as np

def rgb2gray(rgb):

        r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
        gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

        return gray


img = plt.imread('/users/zengxiaohui/Downloads/Picture1.png',0)
img = rgb2gray(img)


print(img.max())
print(img.min())
t = 150
img[np.where(img < t)] = 0
img[np.where(img > t)] = 255
print(img.shape)
#plt.subplot(121),
#a.set_axis_off()


#plt.title('Input Image'), plt.xticks([]), plt.yticks([])
#plt.savefig('/users/zengxiaohui/Downloads/threshold.png')
#plt.show()
fname = "/users/zengxiaohui/Downloads/threshold.png" 
#plt.savefig(fname, bbox_inches='tight', pad_inches=0)
#width = 301
#height = 152
#fig = plt.figure(img, frameon=False)

#fig.set_size_inches((width, height)) 
#ax = plt.Axes(fig, [0., 0., 1., 1.])
#ax.set_axis_off()
#fig.axes.get_xaxis().set_visible(False)
#fig.axes.get_yaxis().set_visible(False)
#fig.subplots_adjust(bottom = 0)
#fig.subplots_adjust(top = 1)
#fig.subplots_adjust(right = 1)
#fig.subplots_adjust(left = 0)
plt.imshow(img, cmap = 'gray')
plt.xticks([]), plt.yticks([])
#plt.show()

#extent = mpl.transforms.Bbox(((0, 0), (width, height))) 
plt.savefig(fname, bbox_inches='tight', pad_inches=0)
