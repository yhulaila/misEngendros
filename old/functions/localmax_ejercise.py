import numpy as np
import pyfits
import skimage.morphology as morph
import skimage.exposure as skie
import matplotlib.pyplot as plt

# Loading astronomy image from an infrared space telescope
img = pyfits.getdata('points.fits')

print (img.shape)
limg = np.zeros((200, 200))
for i in range(0,len(limg)):
    for j in range(0, len(limg)):
        limg[i,j]= img[i+200,j+200]
# Prep file scikit-image environment and plotting
print (limg.shape)
limg = np.arcsinh(limg)
limg = limg / limg.max()
low = np.percentile(limg, 0.25)
high = np.percentile(limg, 99.5)
opt_img = skie.exposure.rescale_intensity(limg, in_range=(low, high))

# Calculating local maxima and filtering out noise
lm = morph.local_maxima(limg)
print (type(lm), len(lm), lm[90,90])
x1, y1 = np.where(lm.T == True)
v = limg[(y1, x1)]
lim = 0.05
x2, y2 = x1[v > lim], y1[v > lim]

# Creating figure to show local maximum detection
# rate success
fig = plt.figure(figsize=(32, 16))
fig.subplots_adjust(hspace=0.05, wspace=0.05)

ax1 = fig.add_subplot(121)
ax1.imshow(opt_img)
ax1.set_xlim(0, limg.shape[1])
ax1.set_ylim(0, limg.shape[0])
ax1.xaxis.set_visible(False)
ax1.yaxis.set_visible(False)

ax2 = fig.add_subplot(122)
ax2.imshow(opt_img)
ax2.scatter(x2, y2, facecolor='#FF0000', edgecolor='#FF0000')
ax2.set_xlim(0, limg.shape[1])
ax2.set_ylim(0, limg.shape[0])
ax2.xaxis.set_visible(False)
ax2.yaxis.set_visible(False)

fig.savefig('points3.jpg', bbox_inches='tight')
