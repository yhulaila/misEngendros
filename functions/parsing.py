import sys
import logging
from planetaryimage import PDS3Image
import matplotlib.pyplot as plt
from matplotlib.cm import jet
from matplotlib.patches import Circle
from matplotlib.collections import PatchCollection



def readpds(filename):

    try:

        pdslabels = PDS3Image.open(filename).label

        inid = pdslabels['INSTRUMENT_ID']

        if inid == 'OSIWAC':
             image = PDS3Image.open(filename).data

        else:
             image = numpy.fliplr(PDS3Image.open(filename).data)


        pdslabels['image_data'] = image
        print (inid)
        image = PDS3Image.open(filename)
        print (plotimage.image)



        masked_array = np.ma.array(image, mask=np.isnan(image))
        cmap = matplotlib.cm.jet
        cmap.set_bad('white', 1.)
        ax.imshow(masked_array, interpolation='nearest', cmap=cmap)

        #plt.imshow(plotimage.image,interpolation='none')
        #plt.show()
        data = PDS3Image.dtype
        print (data)
        print (type(image), len(image), image[0])
        return image


    except:
        e = sys.exc_info()[0]
        logging.error(e)

image = readpds('../test.IMG')