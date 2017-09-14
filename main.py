from functions.algorithms.localmax import take_points
from functions.parsing import readpds
from functions.parsing.clean_values import clean_image

image = readpds('test.IMG')
image = clean_image(image)
print ('Image clean from nan values and charged in memory as', type(image[0]), image[0].shape )
count = image[1]
image = image[0]
print ('number of nan values found = ', count)
print ('##############           Module clean_image executed                       #####################')

stars = take_points(image)

#print ('estrellitas obtenidas', type(stars), stars)
print ('##############           Module take_points executed                       #####################')