import numpy as np
import matplotlib.pyplot as mpl
import skimage.morphology as morph

def take_points(fimg):
    #calculating local maxima
    lm1 = morph.local_maxima(fimg)
    x1, y1 = np.where(lm1.T == True)
    print (x1, type(x1),len(x1))
    print (y1,type(y1),len(y1))
    #creating figures to show local maximum detection
    #rate sucess
    fig = mpl.figure(figsize =(8,8))

    ax = fig.add_subplot(111)
    ax.imshow(fimg)
    ax.scatter(x1, y1, s=100, facecolor='none', edgecolor = '#009999')
    ax.set_xlim(0,400)
    ax.set_ylim(0,200)
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)

    fig.savefig('scikit_image_f03.tif', bbox_inches= 'tight')
    return (' success test')



