
import sys

sys.path.insert(0, '/mnt/PhD/functions/algorithms')
sys.path.insert(0, '/mnt/PhD/functions/parsing')

from localmax import take_points
from parsing import readpds
from clean_values import clean_image
from gaussian_algorithm import get_points

def main(route1):
    route2 = 'manual' + str(route1[6:31]) + '.txt'
    image = readpds(route1)
    print('Image read', type(image))
    image = clean_image(image)
    print ('Image clean from nan values and charged in memory as', type(image[0]) )
    count = image[1]
    image = image[0]

    print ('number of nan values found = ', count)
    print ('##############           Module clean_image executed                       #####################')
    stars = get_points(image)
    print ('estrellitas obtenidas', type(stars), len(stars)/2)
    print ('##############           Module take_points executed                       #####################')
    fichero = open(route2,'w')
    for i in range (0, (int(len(stars)/2-1))):
        fichero.write(str(stars[2*i]))
        fichero.write(str( ','))
        fichero.write(str(stars[2 * i + 1]))
        fichero.write('\n')


    fichero.close()

main('W20150511T083550851ID30F18.IMG')