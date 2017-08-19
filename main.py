from functions.localmax import take_points
from functions.parsing import readpds
import numpy as np


image = readpds('test.IMG')
print ('Image read and charged in memory as', type(image))

#image.shape = (4194304)
stars = take_points(image)