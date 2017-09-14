import numpy as np
import matplotlib.pyplot as plt
import skimage.morphology as morph
import skimage.exposure as skie
import sys

def take_points(img):
    #prep file scikit-image environment and plotting
    #limg = np.arcsinh(img)
    limg = img
    #limg = limg / limg.max()
    #print('después de normalizar, \n valor máximo:  ', np.nanmax(limg), '\n nan media:  ', np.nanmedian(limg))
    #checking no extra nan values added when calculating
    #count2=0
    #for i in range(0, len(limg[0, 0])):
    #    for j in range(0, len(limg[0, 0])):
    #        if np.isnan(limg[0, i, j]):
    #            count2 = count2 + 1
    #print ('total nan values en limg =', count2)

    low = np.percentile(limg, 0.25)
    high = np.percentile(limg, 99.5)
    opt_img = skie.exposure.rescale_intensity(limg, in_range=(low, high))
    #opt_img = limg
    #calculating local maxima and filtering out noise
    lm = morph.local_maxima(limg)
    x1, y1, = np.where(lm.T == True)
    v = limg[( y1, x1)]
    lim = 0.5
    x2, y2 = x1[v > lim], y1[v > lim]

    # Creating figure to show local maximum detection
    # rate success
    fig = plt.figure(figsize=(32, 16))
    fig.subplots_adjust(hspace=0.05, wspace=0.05)

    ax1 = fig.add_subplot(121)
    ax1.imshow(img)
    ax1.set_xlim(0, img.shape[1])
    ax1.set_ylim(0, img.shape[0])
    ax1.xaxis.set_visible(False)
    ax1.yaxis.set_visible(False)

    ax2 = fig.add_subplot(122)
    ax2.imshow(opt_img)
    ax2.scatter(x2, y2, facecolor='#FF7000', edgecolor='#FF7000')
    ax2.set_xlim(0, img.shape[1])
    ax2.set_ylim(0, img.shape[0])
    ax2.xaxis.set_visible(False)
    ax2.yaxis.set_visible(False)

    fig.savefig('local_max_points.jpg', bbox_inches='tight')

