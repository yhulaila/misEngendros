import sys

sys.path.insert(0, '/mnt/PhD/functions/algorithms')
sys.path.insert(0, '/mnt/PhD/functions/parsing')

from localmax import take_points
from parsing import readpds
from clean_values import clean_image


file =  open('data/list.txt')
print(file)
file = file.readlines()
for line in file:
    route1 = str('data/'+line)
    print (route1)
    route2 = 'cache' + str(route1[4:31]) + '.txt'
    print (route2)
    image = readpds(route1)
    image = clean_image(image)
