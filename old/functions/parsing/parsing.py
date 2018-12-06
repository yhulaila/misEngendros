import sys
import logging
from planetaryimage import PDS3Image


def readpds(filename):

    try:

        pdslabels = PDS3Image.open(filename).label

        inid = pdslabels['INSTRUMENT_ID']

        if inid == 'OSIWAC':
             image = PDS3Image.open(filename).data

        else:
             image = numpy.fliplr(PDS3Image.open(filename).data)


        pdslabels['image_data'] = image

        return image

    except:
        e = sys.exc_info()[0]
        logging.error(e)
