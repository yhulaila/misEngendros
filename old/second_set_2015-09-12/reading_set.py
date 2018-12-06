import re
import sys
import glob
from planetaryimage import PDS3Image
import logging



def list_obs():
    route = re.findall('.*/.*?', sys.argv[0] )
    #route = (str(route[0]) + "data/*.IMG")
    route = ("WAC/*.IMG")
    img_names = glob.glob(route)
    file = open("list.txt", "r+")

    for i in range (0,len(img_names)):
        img_names[i]=img_names[i]
        file.writelines(img_names[i])
        file.writelines('\n')

    file.close()
    return img_names

def readpds(filename):

    try:

        pdslabels = PDS3Image.open(filename).label
        inid = pdslabels['INSTRUMENT_ID']

        if inid == 'OSINAC':
             image = PDS3Image.open(filename).data

        elif inid == 'OSIWAC':
             image = PDS3Image.open(filename).data

        else:
             image = numpy.fliplr(PDS3Image.open(filename).data)


        pdslabels['image_data'] = image
        print(len(image), type (image))
        return image

    except:
        e = sys.exc_info()[0]
        logging.error(e)

file = open("list.txt", "r+")

readpds('NAC/N20150912T210002741ID30F22.IMG')

