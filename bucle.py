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
    image = readpds(line)
    print(line, 'read')
