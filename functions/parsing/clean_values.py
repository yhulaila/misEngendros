import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt

def clean_image(img):

    count = 0
    img2 = np.empty((2048,2048))

    for i in range(0, len(img[0, 0])):
        for j in range(0, len(img[0, 0])):
            if np.isnan(img[0, i, j]):
                # nan values to zero to avoid confuse them with dust
                img[0, i, j] = 0
                count = count + 1
            # resize image to be range 2 instead 3
            img2[i,j]=img[0,i,j]

    #fig = plt.figure(figsize=(16, 8))
    #fig.subplots_adjust(hspace=0.05, wspace=0.05)

    #ax1 = fig.add_subplot(121)
    #ax1.imshow(img2)
    #ax1.set_xlim(0, img2.shape[1])
    #ax1.set_ylim(0, img2.shape[0])
    #ax1.xaxis.set_visible(False)
    #ax1.yaxis.set_visible(False)

    #ax2 = fig.add_subplot(122)
    #ax2.imshow(img[0])
    #ax2.set_xlim(0, img[0].shape[1])
    #ax2.set_ylim(0, img[0].shape[0])
    #ax2.xaxis.set_visible(False)
    #ax2.yaxis.set_visible(False)

    #fig.savefig('clean_image_min.jpg', bbox_inches='tight')

    return (img2,count)
