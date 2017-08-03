import sys
#import osirispy
import logging
import numpy
from planetaryimage import PDS3Image


def readpds(filename):

    try:
        #osirispy.check_file(filename)

        pdslabels = PDS3Image.open(filename).label

        inid = pdslabels['INSTRUMENT_ID']

        image = PDS3Image.open(filename).data

        # if inid == 'OSINAC':
        #     image = PDS3Image.open(filename).data
        #
        # else:
        #     image = numpy.fliplr(PDS3Image.open(filename).data)

        pdslabels['image_data'] = image
        print (type(image), len(image), image[0])
        return pdslabels


    except:
        e = sys.exc_info()[0]
        logging.error(e)


