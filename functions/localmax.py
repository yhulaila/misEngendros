import numpy as np
import matplotlib.pyplot as mpl
import skimage.morphology as morph
import skimage.exposure as skie
import sys

def take_points(img):
    #prep file scikit-image environment and plotting

    #limg = np.arcsinh(img)
    print('antes de normalizar', np.nanmax(img), 'media valores', np.nanmedian(img))
    print(img.shape, img.dtype)
    f= open ('antes.txt', 'w')
    f.write(str(img))
    f.close()
    print(len(np.where(np.isnan(img))))

    #mpl.imshow(img, cmap=mpl.cm.gray)
    limg = img / np.nanmedian(img)
    print('después de normalizar', np.nanmax(limg), 'media valores', np.nanmedian(limg))
    g = open('despues.txt', 'w')
    g.write(str(limg))
    g.close()
    print(len(np.where(np.isnan(limg))))
    low = np.percentile(limg, 0.25)
    high = np.percentile(limg, 99.5)
    opt_img = skie.exposure.rescale_intensity(limg, in_range = (low,high))
    #calculating local maxima and filtering out noise
    lm1 = morph.local_maxima(limg)
    print (lm1, len(lm1), type(lm1), lm1.size)
    x1, y1 = np.where(lm1.T == True), np.where(lm1.T == True)
    v = limg[(y1),(x1)]
    lim = 0.5
    x2, y2 = x1[v > lim], y1[v > lim]
    print (x1, type(x1),len(x1))
    print (y1,type(y1),len(y1))
    #creating figures to show local maximum detection
    #rate sucess
    fig = mpl.figure(figsize = (8,4))
    fig.subplots_adjust(hspace = 0.05, wspace = 0.05)

    ax = fig.add_subplot(121)
    ax.imshow(opt_img)
    ax.set_xlim(0,img.shape[1])
    ax.set_ylim(0,img.shape[0])
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)

    ax2 = fig.add_subplot(122)
    ax2.imshow(opt_img)
    fig.savefig('scikit_image_f03.tif', bbox_inches= 'tight')
    return (' success test')



